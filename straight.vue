<template>
    <div class="loader" :class="bindClass"></div>
</template>

<script>
export default {
    name: 'StraightComponent',
    props: {
        height: {
            type: [Number, String],
            default: 100,
        },
        width: {
            type: [Number, String],
            default: 200,
        },
        color: {
            type: String,
            default: 'rgba(0, 0, 0, 12%)',
        },
        animation: {
            type: String,
            default: 'wave',
        },
        type: {
            type: String,
            default: 'rect',
        },
        rounded: {
            type: Boolean,
            default: false,
        },
        radius: {
            type: [Number, String],
            default: 4,
        },
    },
    computed: {
        style() {
            return {
                width:
                    typeof this.width === 'number'
                        ? `${this.width}px`
                        : this.width,
                height:
                    typeof this.width === 'number'
                        ? `${this.height}px`
                        : this.height,
                'background-color': `${this.color}`,
                'border-radius': this.rounded ? `${this.radius}px` : 0,
            }
        },
        bindClass() {
            return `animation--${this.animation} shape--${this.type} shape--${
                this.rounded ? 'round' : 'flat'
            }`
        },
    },
    mounted() {
        const width =
            typeof this.width === 'number' ? `${this.width}px` : this.width
        const height =
            typeof this.width === 'number' ? `${this.height}px` : this.height
        const background = `${this.color}`
        const borderRadius = this.rounded ? `${this.radius}px` : 0
        const loader = this.$el
        loader.style.setProperty('width', width)
        loader.style.setProperty('height', height)
        loader.style.setProperty('background-color', background)
        loader.style.setProperty('border-radius', borderRadius)
    },
}
</script>

<style scoped>
.loader {
    overflow: hidden;

    /* width: 100px;
  height: 100px; */
    position: relative;
}
.loader::before {
    content: '';
    display: block;
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
}

/* Shape stylings */
.shape--text {
    height: 20px;
}
.shape--round {
    border-radius: 8px;
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
