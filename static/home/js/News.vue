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
        <BCard
            v-show="!hide"
            :class="`p-1 mb-1 ${news.pinned ? 'pinned': ''}`"
            no-body
        >
            <BCardTitle>
                {{ news.title }}
            </BCardTitle>
            <BCardSubtitle>
                {{ datetime }}
            </BCardSubtitle>
            <BCardBody class="text-justify">
                <span v-html="news.text" />
                <BButton
                    v-if="store.canAddNews"
                    v-b-modal="`new-${'id' in news ? news.id : 'new'}`"
                >
                    <IBiPencil />
                    Modifier
                </BButton>
                <BButton
                    v-if="store.canAddNews"
                    variant="danger"
                    class="ms-1"
                    @click="$emit('remove')"
                >
                    <IBiTrash />
                    Supprimer
                </BButton>
            </BCardBody>
        </BCard>
        <b-modal
            :id="`new-${'id' in news ? news.id : 'new'}`"
            cancel-title="Annuler"
            @ok="sendData"
        >
            <BFormGroup>
                <BFormCheckbox v-model="pinned">
                    Épingler le message ?
                </BFormCheckbox>
            </BFormGroup>
            <BFormGroup
                label="Titre du message"
            >
                <BFormInput v-model="title" />
            </BFormGroup>
            <BFormGroup>
                <text-editor
                    v-model="text"
                />
            </BFormGroup>
        </b-modal>
    </div>
</template>

<script>
import axios from "axios";

import Moment from "moment";
Moment.locale("fr");

import { useToastController } from "bootstrap-vue-next";

import TextEditor from "@s:core/js/common/text_editor.vue";

import { homeStore } from "./stores/index.js";

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken"};

export default {
    setup: function () {
        const { show } = useToastController();
        return { show };
    },
    emits: ["remove"],
    props: {
        hide: {
            type: Boolean,
            default: false,
        },
        news: {
            type: Object,
            default: () => {
                return {
                    title: "",
                    text: ""
                };
            }
        }
    },
    data: function () {
        return {
            title: "",
            pinned: false,
            text: "",
            store: homeStore(),
        };
    },
    methods: {
        sendData: function () {
            const isNew = !("id" in this.news);
            const send = isNew ? axios.post : axios.put;
            const url = `/home/api/news/${isNew ? "" : this.news.id + "/"}`;
            send(url, {
                title: this.title,
                text: this.text,
                pinned: this.pinned,
            }, token)
                .then(resp => {
                    this.$emit("update", resp.data);
                    if (isNew) {
                        this.title = "";
                        this.text = "";
                        this.pinned = false;
                    }
                })
                .catch(err => {
                    console.log(err);
                    this.show({
                        body: "Une erreur est survenue lors de l'envoi des données.",
                        variant: "danger"
                    });
                });
        }
    },
    computed: {
        datetime: function () {
            return Moment(this.news.datetime_update).calendar();
        }
    },
    mounted: function () {
        this.title = this.news.title;
        this.text = this.news.text;
        this.pinned = this.news.pinned;
    },
    components: {
        TextEditor,
    }
};
</script>

<style>
.pinned {
    border-color: gold;
}
</style>
