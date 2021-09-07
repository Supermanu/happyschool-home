<template>
    <b-col
        v-if="birthdays.length > 0"
        cols="6"
    >
        <b-card class="mb-1">
            <b-card-sub-title>
                Anniversaire du jour
            </b-card-sub-title>
            <b-card-text>
                <b-carousel
                    :interval="3000"
                    no-hover-pause
                >
                    <b-carousel-slide
                        v-for="bd in birthdays"
                        :key="bd.name"
                    >
                        <template #img>
                            {{ bd.name }}
                        </template>
                    </b-carousel-slide>
                </b-carousel>
            </b-card-text>
        </b-card>
    </b-col>
</template>

<script>
import axios from "axios";

export default {
    props: {
        teaching: {
            type: String,
            default: ""
        },
        people: {
            type: String,
            default: "student"
        }
    },
    data: function () {
        return {
            birthdays: []
        };
    },
    mounted: function () {
        axios.get(`/core/api/birthday/?people=${this.people}&teaching=${this.teaching}`)
            .then(resp => {
                this.birthdays = resp.data.results;
            });
    }
};
</script>

<style>
</style>
