<template>
    <div class="game-container">
        <h1>Coloring Fun!</h1>
        <p class="instruction">Pick a color and tap on the shapes below to color them!</p>

        <!-- Color Palette -->
        <div class="color-palette">
            <div v-for="color in colors" :key="color" :style="{ backgroundColor: color }" class="color-box"
                @click="selectedColor = color"></div>
        </div>

        <!-- Colorable Shapes -->
        <div class="shapes-container">
            <div v-for="(shape, index) in shapes" :key="index" :style="{
                backgroundColor: shape.color,
                width: shape.size,
                height: shape.size,
                borderRadius: shape.type === 'circle' ? '50%' : '0',
                border: '2px solid #fff'
            }" @click="colorShape(index)" class="shape"></div>
        </div>

        <p v-if="selectedColor" class="color-selected-message">
            You selected: <span :style="{ color: selectedColor }">{{ selectedColor }}</span>
        </p>
    </div>
</template>

<script>
    import { ref } from 'vue';

    export default {
        name: 'ColoringFun',
        setup() {
            const colors = ['#ff7043', '#ffeb3b', '#4caf50', '#2196f3', '#9c27b0', '#ff4081'];
            const selectedColor = ref('');
            const shapes = ref([
                { type: 'square', color: '#f1f1f1', size: '100px' },
                { type: 'circle', color: '#f1f1f1', size: '100px' },
                { type: 'square', color: '#f1f1f1', size: '150px' },
                { type: 'circle', color: '#f1f1f1', size: '150px' },
            ]);

            const colorShape = (index) => {
                if (!selectedColor.value) {
                    alert('Please select a color first!');
                    return;
                }
                shapes.value[index].color = selectedColor.value;
            };

            return {
                colors,
                selectedColor,
                shapes,
                colorShape,
            };
        },
    };
</script>

<style scoped>
    .game-container {
        text-align: center;
        padding: 20px;
        background-color: #e1f5fe;
        font-family: 'Comic Sans MS', sans-serif;
    }

    h1 {
        color: #ff7043;
        font-size: 36px;
        margin-bottom: 20px;
    }

    .instruction {
        font-size: 18px;
        color: #6c757d;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .color-palette {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
        flex-wrap: wrap;
    }

    .color-box {
        width: 50px;
        height: 50px;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }

    .color-box:hover {
        transform: scale(1.1);
    }

    .shapes-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 30px;
        flex-wrap: wrap;
    }

    .shape {
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .shape:hover {
        transform: scale(1.1);
    }

    .color-selected-message {
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        color: #388e3c;
    }

    @media (max-width: 1024px) {
        h1 {
            font-size: 32px;
        }

        .color-box {
            width: 45px;
            height: 45px;
        }

        .shape {
            width: 120px;
            height: 120px;
        }
    }

    @media (max-width: 768px) {
        h1 {
            font-size: 28px;
        }

        .color-box {
            width: 40px;
            height: 40px;
        }

        .shape {
            width: 100px;
            height: 100px;
        }
    }

    @media (max-width: 480px) {
        h1 {
            font-size: 24px;
        }

        .color-box {
            width: 35px;
            height: 35px;
        }

        .shape {
            width: 80px;
            height: 80px;
        }

        .instruction {
            font-size: 16px;
        }

        .color-selected-message {
            font-size: 18px;
        }
    }

    @media (max-width: 360px) {
        .color-box {
            width: 30px;
            height: 30px;
        }

        .shape {
            width: 70px;
            height: 70px;
        }

        .instruction {
            font-size: 14px;
        }
    }
</style>
