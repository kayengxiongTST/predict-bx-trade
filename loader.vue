<template>
    <circle-loader
        v-if="type === 'circle'"
        :width="loaderWidth"
        :height="loaderHeight"
        :animation="animation"
        :color="color"
    />
    <square-loader
        v-else
        :width="loaderWidth"
        :height="loaderHeight"
        :animation="animation"
        :type="type"
        :color="color"
        :rounded="rounded"
        :radius="radius"
    />
</template>

<script>
import CircleLoader from './Pices/Circle.vue'
import SquareLoader from './Pices/Straight.vue'
export default {
    name: 'LoaderComponent',
    components: {
        CircleLoader,
        SquareLoader,
    },
    props: {
        type: {
            type: String,
            default: 'rect',
        },
        size: {
            type: [Number, String],
            default: '',
        },
        animation: {
            type: String,
            default: 'wave',
        },
        height: {
            type: [Number, String],
            default: '20px',
        },
        width: {
            type: [Number, String],
            default: '100%',
        },
        color: {
            type: String,
            default: 'rgba(0, 0, 0, 12%)',
        },
        waveColor: {
            type: String,
            default: 'rgba(255, 255, 255, 10%)',
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
        loaderWidth() {
            if (this.size) {
                return this.size
            } else {
                return this.width
            }
        },
        loaderHeight() {
            if (this.size) {
                return this.size
            } else {
                return this.height
            }
        },
    },
    mounted() {
        if (this.waveColor) {
            this.$el.style.setProperty('--gradient-color', this.waveColor)
        }
    },
}
</script>

<style lang="css">
.loader {
    width: fit-content;

    --gradient-color: rgba(255, 255, 255, 10%);
}

/* Animation definitions */
@keyframes fade {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0.4;
    }
    100% {
        opacity: 1;
    }
}
@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(0.85);
    }
    100% {
        transform: scale(1);
    }
}
@keyframes pulse-x {
    0% {
        transform: scaleX(1);
    }
    50% {
        transform: scaleX(0.75);
    }
    100% {
        transform: scaleX(1);
    }
}
@keyframes pulse-y {
    0% {
        transform: scaleY(1);
    }
    50% {
        transform: scaleY(0.75);
    }
    100% {
        transform: scaleY(1);
    }
}
@keyframes wave {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(100%);
    }
}

/* Animation classes */
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
