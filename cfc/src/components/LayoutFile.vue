<template>
    <div class="landing-page">
        <!-- Header Section -->
        <header class="header">
            <NavBar />
        </header>

        <!-- Hero Section -->
        <section v-if="currentRoute === '/'" class="hero-section">
            <HeroPage   />
        </section>

        <!-- Features Section -->
        <section id="features" class="features">
            <RouterView />

        </section>

        <!-- Footer Section -->
        <footer class="footer">
            <p>&copy; 2024 OPENCFFS. All Rights Reserved.</p>
        </footer>

        <!-- Thank You Badge Modal -->
        <div v-if="showBadge" class="thank-you-modal">
            <div class="modal-content">
                <h2>Thank You!</h2>
                <p>You've made a difference today!</p>
                <button @click="closeBadge">Close</button>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import ChildFriendlyCard from "@/components/ChildFriendlyCard.vue";
import NavBar from "./NavBar.vue";
import HeroPage from "./HeroPage.vue";


export default {
  components: {
    ChildFriendlyCard,
    NavBar,
    HeroPage,
  },
  setup() {
    const router = useRouter();
    const showBadge = ref(false);
    const route = useRoute();
    const currentRoute = ref(route.path);
    watch(route, () => {
      currentRoute.value = route.path;
    });

    
    const closeBadge = () => {
      showBadge.value = false;
    };

    

    return {
      showBadge,
      closeBadge,
      currentRoute,
    };
  },
};
</script>


<style scoped>
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin-top: 2rem;
        justify-items: center;
        padding: 0 1rem;
    }

    @media (max-width: 768px) {
        .features-grid {
            grid-template-columns: 1fr;
            gap: 1.25rem;
        }
    }
</style>
