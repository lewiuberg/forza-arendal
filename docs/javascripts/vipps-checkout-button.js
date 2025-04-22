// Ensure the Vipps Checkout library is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Create a container for the button
  const buttonContainer = document.getElementById("vipps-button-container");

  if (buttonContainer) {
    // Initialize the Vipps Checkout button
    const vippsButton = VippsCheckoutButton.create({
      clientId: "your-client-id", // Replace with your actual client ID
      merchantRedirectUrl: "https://your-redirect-url.com", // Replace with your redirect URL
      locale: "nb", // Optional: Set the locale (e.g., 'nb' for Norwegian Bokmål)
    });

    // Append the button to the container
    buttonContainer.appendChild(vippsButton);
  } else {
    console.error("Vipps button container not found!");
  }
});
