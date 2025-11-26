let cart = [];

const cartBtn = document.getElementById("cart-btn");
const cartPanel = document.getElementById("cart-panel");
const closeCart = document.getElementById("close-cart");
const cartCount = document.getElementById("cart-count");
const cartItemsDiv = document.getElementById("cart-items");
const totalPrice = document.getElementById("total-price");
const checkoutBtn = document.getElementById("checkout-btn");

/* Mostrar / Ocultar Carrito */
cartBtn.addEventListener("click", () => cartPanel.classList.add("show"));
closeCart.addEventListener("click", () => cartPanel.classList.remove("show"));

/* Añadir producto */
function addToCart(id, name, price, image) {
    const item = cart.find((p) => p.id === id);

    if (item) item.quantity++;
    else cart.push({ id, name, price, image, quantity: 1 });

    updateCart();
}

/* Actualizar carrito */
function updateCart() {
    cartCount.textContent = cart.reduce((a, item) => a + item.quantity, 0);

    cartItemsDiv.innerHTML = "";
    let total = 0;

    cart.forEach((item) => {
        total += item.price * item.quantity;

        const div = document.createElement("div");
        div.className = "cart-item";

        div.innerHTML = `
            <img src="${item.image}" class="cart-img">
            <div class="cart-info">
                <h4>${item.name}</h4>
                <p>$${item.price}</p>
                <div class="cart-controls">
                    <button onclick="changeQty(${item.id}, -1)">-</button>
                    <span>${item.quantity}</span>
                    <button onclick="changeQty(${item.id}, 1)">+</button>
                </div>
            </div>
        `;

        cartItemsDiv.appendChild(div);
    });

    totalPrice.textContent = "$" + total;
}

/* Cambiar cantidad */
function changeQty(id, val) {
    const item = cart.find((i) => i.id === id);
    if (!item) return;

    item.quantity += val;
    if (item.quantity <= 0) cart = cart.filter((i) => i.id !== id);

    updateCart();
}

/* Checkout con Stripe */
checkoutBtn.addEventListener("click", async () => {
    if (cart.length === 0) return;

    const res = await fetch("/create-checkout-session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cart }),
    });

    const data = await res.json();
    if (data.url) window.location.href = data.url;
});