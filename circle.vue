<template>
    <div class="loader loader--circle" :class="bindClass"></div>
</template>

<script>
export default {
    name: 'CircleComponent',
    props: {
        height: {
            type: [Number, String],
            default: 100,
        },
        width: {
            type: [Number, String],
            default: 100,
        },
        color: {
            type: String,
            default: 'rgba(0, 0, 0, 12%)',
        },
        animation: {
            type: String,
            default: 'wave',
        },
    },
    computed: {
        bindClass() {
            return `animation--${this.animation}`
        },
    },
    mounted() {
        const width =
            typeof this.width === 'number' ? `${this.width}px` : this.width
        const height =
            typeof this.width === 'number' ? `${this.height}px` : this.height
        const background = `${this.color}`
        const loader = this.$el
        loader.style.setProperty('width', width)
        loader.style.setProperty('height', height)
        loader.style.setProperty('background-color', background)
    },
}
</script>

<style scoped>
.loader--circle {
    overflow: hidden;
    width: 100px;
    height: 100px;
    background-color: red;
    border-radius: 50%;
    position: relative;
}
.loader--circle::before {
    content: '';
    display: block;
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
}
  .animation--fade {
    animation: fade 1.5s linear 0.5s infinite;
}
.animation--wave::before {
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 50%),
        transparent
    );
    background: linear-gradient(
        90deg,
        transparent,
        var(--gradient-color),
        transparent
    );
    animation: wave 1.5s linear 0.5s infinite;
}
.animation--pulse-x {
    animation: pulse-x 1.5s linear 0.5s infinite;
}
.animation--pulse-y {
    animation: pulse-y 1.5s linear 0.5s infinite;
}
.animation--pulse {
    animation: pulse 1.5s linear 0.5s infinite;
}
</style>
