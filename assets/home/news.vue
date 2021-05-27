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
    <div>
        <b-card
            :class="`p-1 mb-1 ${news.pinned ? 'pinned': ''}`"
            no-body
        >
            <b-card-title>
                {{ news.title }}
            </b-card-title>
            <b-card-sub-title>
                {{ datetime }}
            </b-card-sub-title>
            <b-card-body class="text-justify">
                <span v-html="news.text" />
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
import Moment from "moment";
Moment.locale("fr");

export default {
    props: {
        news: {
            type: Object,
            default: () => {
                return {
                    title: "Titre",
                    text: "Le texte de la nouvelle."
                };
            }
        }
    },
    computed: {
        datetime: function () {
            return Moment(this.news.datetime_update).calendar();
        }
    }
};
</script>

<style>
.pinned {
    border-color: gold;
}
</style>
