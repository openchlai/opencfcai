<template>
    <div class="hero">
        <div class="login-form">
            <h1>Login</h1>
            <form @submit.prevent="handleLogin">
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" v-model="email" required placeholder="Enter your email" />
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" v-model="password" required
                        placeholder="Enter your password" />
                </div>
                <button type="submit" :disabled="isLoading">
                    {{ isLoading ? "Loading..." : "Login" }}
                </button>
                <p v-if="error" class="error-message">{{ error }}</p>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { ref } from "vue";
    import { useRouter } from "vue-router";

    const router = useRouter();
    const email = ref("");
    const password = ref("");
    const error = ref("");
    const isLoading = ref(false);

    const handleLogin = async () => {
        try {
            isLoading.value = true;
            error.value = "";

            // Add your authentication logic here
            router.push("/dashboard");
        } catch (err) {
            error.value = err.message || "Failed to login";
        } finally {
            isLoading.value = false;
        }
    };
</script>
