<template>
    <div class="child-help-page">
        <header class="header">
            <h1>We're Here to Help</h1>
            <p>Feel free to share anything. You're safe here.</p>
        </header>

        <div class="chat-container">
            <div class="chat-window">
                <div v-for="(message, index) in messages" :key="index" :class="message.type">
                    <p>{{ message.text }}</p>
                </div>
            </div>
            <form @submit.prevent="sendMessage" class="chat-input">
                <input v-model="userInput" type="text" :placeholder="currentPrompt.placeholder"
                    aria-label="Type your message" :disabled="isSubmitting" />
                <button type="submit" :disabled="isSubmitting">Send</button>
            </form>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                userInput: "",
                messages: [
                    { text: "Hello! I'm here to help you sign up. What's your name? 😊", type: "bot" },
                ],
                form: {
                    name: "",
                    age: null,
                    gender: "",
                    parentEmail: "",
                    interests: "",
                    consent: false,
                },
                currentStep: "name",
                isSubmitting: false,
                prompts: {
                    name: { text: "What's your name? 😊", placeholder: "Enter your first name" },
                    age: { text: "How old are you? 🎂", placeholder: "Enter your age (1-18)" },
                    gender: {
                        text: "What's your gender? 🧒",
                        placeholder: "Enter: boy, girl, other, or prefer not to say",
                    },
                    parentEmail: {
                        text: "Parent/Guardian Email 📧",
                        placeholder: "Enter your parent's email",
                    },
                    interests: {
                        text: "What do you like? 🌈",
                        placeholder: "E.g., games, books, sports",
                    },
                    consent: {
                        text: "Do you have your parent's/guardian's permission to sign up? Type 'yes' to confirm. ✅",
                        placeholder: "Type 'yes' or 'no'",
                    },
                    finished: {
                        text: "Thank you for signing up! 🎉 You're all set to begin.",
                        placeholder: "",
                    },
                },
            };
        },
        computed: {
            currentPrompt() {
                return this.prompts[this.currentStep];
            },
        },
        methods: {
            sendMessage() {
                if (this.userInput.trim() === "") return;

                // Add user's message to the chat
                this.messages.push({ text: this.userInput, type: "user" });

                const input = this.userInput.trim();
                this.userInput = "";

                setTimeout(() => {
                    this.handleResponse(input);
                }, 500);
            },
            handleResponse(input) {
                if (this.currentStep === "name") {
                    this.form.name = input;
                    this.advanceStep("age");
                } else if (this.currentStep === "age") {
                    const age = parseInt(input, 10);
                    if (age >= 1 && age <= 18) {
                        this.form.age = age;
                        this.advanceStep("gender");
                    } else {
                        this.addBotMessage("Please enter a valid age between 1 and 18.");
                    }
                } else if (this.currentStep === "gender") {
                    const validGenders = ["boy", "girl", "other", "prefer not to say"];
                    if (validGenders.includes(input.toLowerCase())) {
                        this.form.gender = input;
                        this.advanceStep("parentEmail");
                    } else {
                        this.addBotMessage("Please enter a valid gender option.");
                    }
                } else if (this.currentStep === "parentEmail") {
                    if (this.validateEmail(input)) {
                        this.form.parentEmail = input;
                        this.advanceStep("interests");
                    } else {
                        this.addBotMessage("Please enter a valid email address.");
                    }
                } else if (this.currentStep === "interests") {
                    this.form.interests = input;
                    this.advanceStep("consent");
                } else if (this.currentStep === "consent") {
                    if (input.toLowerCase() === "yes") {
                        this.form.consent = true;
                        this.advanceStep("finished");
                    } else {
                        this.addBotMessage("You need your parent's/guardian's permission to sign up.");
                    }
                }
            },
            advanceStep(nextStep) {
                this.currentStep = nextStep;
                if (nextStep === "finished") {
                    this.addBotMessage(this.prompts[nextStep].text);
                    console.log("Collected Form Data:", this.form); // Here you can handle the form submission logic.
                } else {
                    this.addBotMessage(this.prompts[nextStep].text);
                }
            },
            addBotMessage(text) {
                this.messages.push({ text, type: "bot" });
            },
            validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            },
        },
    };
</script>

<style scoped>
    /* Retain your existing styles */
</style>
