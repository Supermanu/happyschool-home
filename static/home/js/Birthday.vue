<!-- This file is part of Happyschool. -->
<!--  -->
<!-- Happyschool is the legal property of its developers, whose names -->
<!-- can be found in the AUTHORS file distributed with this source -->
<!-- distribution. -->
<!--  -->
<!-- Happyschool is free software: you can redistribute it and/or modify -->
<!-- it under the terms of the GNU Affero General Public License as published by -->
<!-- the Free Software Foundation, either version 3 of the License, or -->
<!-- (at your option) any later version. -->
<!--  -->
<!-- Happyschool is distributed in the hope that it will be useful, -->
<!-- but WITHOUT ANY WARRANTY; without even the implied warranty of -->
<!-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the -->
<!-- GNU Affero General Public License for more details. -->
<!--  -->
<!-- You should have received a copy of the GNU Affero General Public License -->
<!-- along with Happyschool.  If not, see <http://www.gnu.org/licenses/>. -->

<template>
    <BCol
        v-if="birthdays.length > 0"
        cols="6"
    >
        <BCard class="mb-1">
            <BCardSubtitle>
                Anniversaire du jour
            </BCardSubtitle>
            <BCardText>
                <BCarousel
                    :interval="3000"
                    no-hover-pause
                    ride="carousel"
                >
                    <BCarouselSlide
                        v-for="bd in birthdays"
                        :key="bd.name"
                        background="transparent"
                    >
                        <template #img>
                            {{ bd.name }}
                        </template>
                    </BCarouselSlide>
                </BCarousel>
            </BCardText>
        </BCard>
    </BCol>
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
