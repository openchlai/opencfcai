<template>
    <nav class="nav-bar">
        <!-- Back Button -->

        <div>
            <button class="back-btn" @click="navigateBack"><i class="bi bi-arrow-left"></i> Back</button>
        </div>
        <!-- Home Icon -->
        <div class="home-icon" @click="navigateHome">
            <span>🏠</span>
        </div>

        <div>

            <!-- Menu Toggle for Mobile -->
            <button class="menu-toggle" @click="toggleMenu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </button>
            <!-- Navigation Links -->
            <ul :class="{ 'nav-links': true, 'nav-active': isMenuOpen }">
                <li><a href="#features">Features</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>


    </nav>

</template>

<script>
    import { ref } from "vue";
    import { useRouter } from "vue-router";

    export default {
        setup() {
            const isMenuOpen = ref(false);
            const router = useRouter();

            const toggleMenu = () => {
                isMenuOpen.value = !isMenuOpen.value;
            };

            const navigateHome = () => {
                router.push("/");
            };

            const navigateBack = () => {
                router.back();
            };

            return {
                isMenuOpen,
                toggleMenu,
                navigateHome,
                navigateBack,
            };
        },
    };
</script>
