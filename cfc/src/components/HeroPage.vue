<template>
        <div class="hero">
            <div class="hero-content">
                <h1>Welcome to <span class="highlight">OPENCFFS</span></h1>
                <p class="hero-text">
                    A safe space for children and families. <br />
                    Share your voice, find help, and grow stronger together.
                </p>
                <button class="cta-button" @click="navigateToStart">
                    🌟 Get Started
                </button>
            </div>
            <div class="hero-image">
                <img src="https://via.placeholder.com/400x300" alt="Happy children illustration" />
            </div>
        </div>

</template>

<script>
    import { useRouter } from "vue-router";

    export default {
        setup() {
            const router = useRouter();
            const navigateToStart = () => {
                window.location.replace("/safe-sharing");
            };

            return {
                navigateToStart,
            };
        },
    };
</script>
