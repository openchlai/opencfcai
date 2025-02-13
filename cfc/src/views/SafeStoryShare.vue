<template>
  <div class="safe-sharing-container">
    <!-- Header Section -->
    <header class="safe-sharing-header">
      <h1>Welcome to Safe Sharing!</h1>
      <p>Express yourself in a secure and non-judgmental environment.</p>
    </header>

    <!-- Features Section -->
    <section class="features">
      <div class="feature-card" v-for="feature in features" :key="feature.title">
        <img :src="feature.icon" :alt="feature.title" class="feature-icon" />
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.description }}</p>
      </div>
    </section>

    <!-- Mood Selector -->
    <section class="mood-selector">
      <h2>How are you feeling today?</h2>
      <div class="mood-options">
        <button v-for="mood in moods" :key="mood.name"
          :class="['mood-button', { selected: mood.name === selectedMood }]" @click="selectMood(mood.name)">
          <img :src="mood.icon" :alt="mood.name" />
          <span>{{ mood.name }}</span>
        </button>
      </div>
    </section>

    <!-- Story Prompt Section -->
    <section class="story-prompt">
      <h2>{{ moodBasedTitle }}</h2>
      <p class="prompt">{{ moodBasedPrompt }}</p>
      <textarea v-model="story" placeholder="Type your story here..." class="story-input"></textarea>
      <button class="share-button" @click="shareStory" v-if="story.trim() !== ''">Share Now</button>
    </section>

    <!-- Drawing Board -->
    <section class="drawing-board">
      <h2>Draw Your Feelings</h2>
      <canvas ref="drawingCanvas" class="canvas">
        <DrawingBoard />
      </canvas>
      <button class="clear-drawing" @click="clearCanvas">Clear Drawing</button>
    </section>

    <!-- Play Games Section -->
    <section class="play-games" v-if="activateGames">
      <h2>Play Games</h2>
      <div class="games-container">
        <InteractiveGames />
      </div>
    </section>



    <!-- Support Section -->
    <section class="support">
      <h2>Need Help?</h2>
      <p>We’re here for you anytime. Reach out to us below:</p>
      <button class="contact-button" @click="navigateToChildHelp">Chat with Us</button>
    </section>
  </div>
</template>

<script>
  import { ref, computed, onMounted } from "vue";
  import { useRouter } from "vue-router";
  import angryIcon from "@/assets/Icons/angry_11732053.png";
  import sadIcon from "@/assets/Icons/sad-face_11068997.png";
  import confuseIcon from "@/assets/Icons/confused_4818761.png";
  import happyIcon from "@/assets/Icons/winking-face_10963369.png";
  import confidential from "@/assets/Icons/confidential_16659660.png";
  import interactive from "@/assets/Icons/interaction_11296524.png";
  import supportive from "@/assets/Icons/supportive_16137493.png";
  import DrawingBoard from "@/components/DrawingBoard.vue";
  import InteractiveGames from "./InteractiveGames.vue";

  export default {
    components: {
      DrawingBoard,
      InteractiveGames,
    },
    setup() {
      const features = ref([
        {
          icon: confidential,
          title: "Confidentiality Guarantee",
          description: "Your stories are private and protected.",
        },
        {
          icon: interactive,
          title: "Interactive Sharing",
          description: "Express yourself with text, voice, or emojis.",
        },
        {
          icon: supportive,
          title: "Supportive Responses",
          description: "Receive kind replies from our trained helpers.",
        },
      ]);

      const moods = ref([
        { name: "Happy", icon: happyIcon },
        { name: "Sad", icon: sadIcon },
        { name: "Angry", icon: angryIcon },
        { name: "Confused", icon: confuseIcon },
      ]);

      const moodPrompts = {
        Happy: {
          title: "Share Your Joyful Moments",
          prompt: "What made you smile or feel happy today?",
        },
        Sad: {
          title: "Share Your Sorrows",
          prompt: "What's been troubling you? We're here to listen.",
        },
        Angry: {
          title: "Share Your Frustrations",
          prompt: "What made you angry? Let it out and express yourself.",
        },
        Confused: {
          title: "Share Your Thoughts",
          prompt: "What's puzzling or confusing you? Feel free to share.",
        },
      };

      const router = useRouter();

      const selectedMood = ref(null);
      const story = ref("");

      const moodBasedTitle = computed(() =>
        selectedMood.value ? moodPrompts[selectedMood.value].title : "Share Your Story"
      );

      const moodBasedPrompt = computed(() =>
        selectedMood.value ? moodPrompts[selectedMood.value].prompt : "How are you feeling today? Let us know."
      );

      const feedback = ref([]);

      const selectMood = (moodName) => {
        selectedMood.value = moodName;
        story.value = ""; // Clear the story when changing moods
        feedback.value = ""; // Clear the feedback when changing moods
      };

      const shareStory = () => {
        const trimmedStory = story.value.trim();
        if (trimmedStory) {
          console.log("Mood:", selectedMood.value);
          console.log("Story:", trimmedStory);
          activateGames.value = true;
          alert("Your story has been shared!");
          story.value = "";
          feedback.value.push({
            mood: selectedMood.value,
            story: trimmedStory,
          });
        } else {
          alert("Please write something before sharing.");
        }
      };

      const drawingCanvas = ref(null);
      const activateGames = ref(false);

      const clearCanvas = () => {
        const canvas = drawingCanvas.value;
        const context = canvas.getContext("2d");
        context.clearRect(0, 0, canvas.width, canvas.height);
      };

      const navigateToChildHelp = () => {
        // Implement navigation logic here
        router.push("/child-help");
      };

      onMounted(() => {
        const canvas = drawingCanvas.value;
        const context = canvas.getContext("2d");

        canvas.width = 300;
        canvas.height = 300;

        canvas.addEventListener("mousedown", (e) => {
          context.beginPath();
          context.moveTo(e.offsetX, e.offsetY);
          canvas.addEventListener("mousemove", draw);
        });

        canvas.addEventListener("mouseup", () => {
          canvas.removeEventListener("mousemove", draw);
        });

        const draw = (e) => {
          context.lineTo(e.offsetX, e.offsetY);
          context.strokeStyle = "black";
          context.lineWidth = 2;
          context.stroke();
        };
      });

      return {
        features,
        moods,
        selectedMood,
        moodBasedTitle,
        moodBasedPrompt,
        story,
        selectMood,
        shareStory,
        clearCanvas,
        drawingCanvas,
        activateGames,
        feedback,
        navigateToChildHelp,
      };
    },
  };
</script>

<style scoped>
  /* Add your styles here */
</style>
