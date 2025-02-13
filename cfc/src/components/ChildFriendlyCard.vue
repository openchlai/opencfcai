<template>
    <div class="card">
        <div class="card-header">
            <slot name="header">
                <h2>Default Title</h2>
            </slot>
        </div>
        <div class="card-body">
            <slot>
                <p>This is default card content. Replace it with your own!</p>
            </slot>
        </div>
        <div class="card-footer">
            <slot name="footer">
                <button class="card-button">Learn More</button>
            </slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ChildFriendlyCard",
    };
</script>

<style scoped>
    .card {
        background-color: #f8f9fa;
        border-radius: 16px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 300px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .card-header {
        background-color: #ffe4b5;
        border-radius: 16px 16px 0 0;
        padding: 1rem;
        font-size: 1.5rem;
        color: #333;
    }

    .card-body {
        padding: 1rem;
        font-size: 1rem;
        color: #666;
    }

    .card-footer {
        margin-top: 1rem;
    }

    .card-button {
        background-color: #4caf50;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1rem;
        transition: background-color 0.3s ease;
    }

    .card-button:hover {
        background-color: #45a049;
    }
</style>
