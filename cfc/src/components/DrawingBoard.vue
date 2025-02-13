<template>
    <div class="drawing-board">
        <h2>Draw Your Feelings</h2>
        <canvas ref="drawingCanvas" class="canvas" @mousedown="startDrawing" @mousemove="draw" @mouseup="stopDrawing"
            @mouseleave="stopDrawing" @touchstart="startDrawing" @touchmove="draw" @touchend="stopDrawing"></canvas>
        <div class="controls">
            <button class="clear-drawing" @click="clearCanvas">Clear Drawing</button>
            <button class="save-drawing" @click="saveDrawing">Save Drawing</button>
        </div>
    </div>
</template>

<script>
    import { ref, onMounted } from "vue";

    export default {
        name: "DrawingBoard",
        setup() {
            const drawingCanvas = ref(null);
            const isDrawing = ref(false);
            let ctx = null;

            const canvasWidth = 400;
            const canvasHeight = 300;

            onMounted(() => {
                const canvas = drawingCanvas.value;
                canvas.width = canvasWidth;
                canvas.height = canvasHeight;
                ctx = canvas.getContext("2d");
                ctx.lineWidth = 2;
                ctx.lineCap = "round";
                ctx.strokeStyle = "#000";
            });

            const startDrawing = (event) => {
                isDrawing.value = true;
                const { offsetX, offsetY } = getEventCoordinates(event);
                ctx.beginPath();
                ctx.moveTo(offsetX, offsetY);
            };

            const draw = (event) => {
                if (!isDrawing.value) return;
                const { offsetX, offsetY } = getEventCoordinates(event);
                ctx.lineTo(offsetX, offsetY);
                ctx.stroke();
            };

            const stopDrawing = () => {
                isDrawing.value = false;
                ctx.closePath();
            };

            const clearCanvas = () => {
                const canvas = drawingCanvas.value;
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            };

            const saveDrawing = () => {
                const canvas = drawingCanvas.value;
                const dataURL = canvas.toDataURL("image/png");
                const link = document.createElement("a");
                link.href = dataURL;
                link.download = "drawing.png";
                link.click();
            };

            const getEventCoordinates = (event) => {
                if (event.touches && event.touches[0]) {
                    const rect = drawingCanvas.value.getBoundingClientRect();
                    return {
                        offsetX: event.touches[0].clientX - rect.left,
                        offsetY: event.touches[0].clientY - rect.top,
                    };
                }
                return {
                    offsetX: event.offsetX,
                    offsetY: event.offsetY,
                };
            };

            return {
                drawingCanvas,
                startDrawing,
                draw,
                stopDrawing,
                clearCanvas,
                saveDrawing,
            };
        },
    };
</script>

<style scoped>
    .drawing-board {
        text-align: center;
        margin: 20px;
    }

    .canvas {
        border: 1px solid #ccc;
        display: block;
        margin: 0 auto 20px;
        touch-action: none;
        /* Prevent touch scrolling while drawing */
    }

    .controls {
        display: flex;
        justify-content: center;
        gap: 10px;
    }

    .clear-drawing,
    .save-drawing {
        padding: 10px 20px;
        background-color: #4caf50;
        color: white;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        font-size: 1rem;
        transition: background-color 0.2s;
    }

    .clear-drawing:hover {
        background-color: #f44336;
    }

    .save-drawing:hover {
        background-color: #45a049;
    }
</style>
