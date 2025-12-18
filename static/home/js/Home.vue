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
        <BContainer>
            <BRow>
                <BCol
                    cols="12"
                    md="8"
                >
                    <BRow>
                        <birthdays people="responsible" />
                        <birthdays
                            people="student"
                            :teaching="teaching"
                        />
                    </BRow>
                    <BRow>
                        <BCol>
                            <BButton
                                v-if="store.canAddNews"
                                variant="success"
                                v-b-modal.new-new
                                class="mb-1"
                            >
                                <IBiPlus />
                                Ajouter une nouvelle
                            </BButton>
                        </BCol>
                    </BRow>
                    <BOverlay :show="loadingNews">
                        <news
                            :hide="true"
                            @update="createNews"
                        />
                        <news
                            v-for="(n, index) in news"
                            :key="n.id"
                            :news="n"
                            @update="updateNews(index, $event)"
                            @remove="removeNews(index)"
                        />
                    </BOverlay>
                </BCol>
                <BCol
                    cols="12"
                    md="4"
                >
                    <emails />
                    <BCard
                        no-body
                        class="mb-2"
                    >
                        <BListGroup flush>
                            <BListGroupItem>
                                <strong>
                                    Prochains événements
                                </strong>
                            </BListGroupItem>
                            <BListGroupItem
                                v-for="(event, index) in events"
                                :key="index"
                            >
                                <span
                                    v-if="event.begin === event.end || !event.end"
                                    class="date"
                                >
                                    Le {{ event.begin }}
                                </span>
                                <span
                                    v-else
                                    class="date"
                                >
                                    Du {{ event.begin }} au {{ event.end }}
                                </span>
                                <br>
                                {{ event.name }}
                            </BListGroupItem>
                            <BListGroupItem>
                                <a
                                    href="https://www.isln.be/actualite/calendrier/"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    <IBiBoxArrowUpRight />
                                    Tous les événements
                                </a>
                            </BListGroupItem>
                        </BListGroup>
                    </BCard>
                </BCol>
            </BRow>
            <BRow class="text-center">
                <BCol
                    cols="12"
                    md="3"
                >
                    <div class="px-5 px-md-0">
                        <a
                            href="https://eplateforme.isln.be/"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                :src="'/static/home/img/logo_moodle.png'"
                                alt="Moodle logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </BCol>
                <BCol
                    cols="12"
                    md="3"
                >
                    <div class="px-5 px-md-0">
                        <a
                            href="http://pythomium.net/bul/sl_namur.html"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                :src="'/static/home/img/logo_bulrezo.png'"
                                alt="bulrézo logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </BCol>
                <BCol
                    cols="12"
                    md="3"
                >
                    <div class="px-5 px-md-0">
                        <a
                            href="https://institut-saint-louis.webuntis.com/"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                :src="'/static/home/img/logo_untis.png'"
                                alt="WebUntis logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </BCol>
                <BCol
                    cols="12"
                    md="3"
                >
                    <div class="px-5 px-md-0">
                        <a
                            href="https://isln.it-school.be/"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                :src="'/static/home/img/logo_it-school.png'"
                                alt="it-school logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </BCol>
            </BRow>
        </BContainer>
    </div>
</template>

<script>
import axios from "axios";

import { homeStore } from "./stores/index.js";

import { useModalController } from "bootstrap-vue-next";

import News from "./News.vue";
import Birthdays from "./Birthday.vue";
import Emails from "./Emails.vue";

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" };

export default {
    setup: function () {
        const { create } = useModalController();
        return { create };
    },
    data: function () {
        return {
            news: [],
            events: [],
            loadingNews: false,
            store: homeStore(),
        };
    },
    computed: {
        teaching: function () {
            // eslint-disable-next-line no-undef
            const user_teaching = user_properties.teaching;
            if (user_teaching.length > 1 || user_teaching.length == 0) {
                return "";
            } else {
                return user_teaching[0];
            }
        },
    },
    methods: {
        updateNews: function (newsIndex, data) {
            this.news.splice(newsIndex, 1, data);
        },
        createNews: function () {
            this.getNews();
        },
        removeNews: function (newsIndex) {
            this.create({
                body: "Êtes-vous sûr de vouloir supprimer cette nouvelle ?",
                title: "Confirmation",
                size: "sm",
                buttonSize: "sm",
                okVariant: "danger",
                okTitle: "Oui",
                cancelTitle: "Non",
                footerClass: "p-2",
                hideHeaderClose: false,
                centered: true,
            })
                .then((resp) => {
                    if (resp.ok) {
                        axios.delete(`/home/api/news/${this.news[newsIndex].id}/`, token)
                            .then(() => {
                                this.getNews();
                            })
                            .catch((err) => {
                                console.log(err);
                            });
                    }
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        getNews: function () {
            this.loadingNews = true;
            axios.get("/home/api/news/")
                .then((resp) => {
                    this.loadingNews = false;
                    this.news = resp.data.results;
                })
                .catch((err) => {
                    console.log(err);
                    this.loadingNews = false;
                });
        },
        getCalendar: function () {
            axios.get("/core/api/calendar/")
                .then((resp) => {
                    this.events = resp.data.results.slice(0, 5);
                });
        },
    },
    mounted: function () {
        this.getNews();
        this.getCalendar();
    },
    components: {
        News,
        Birthdays,
        Emails,
    },
};
</script>

<style>
.question {
    width: 1.5em;
    height: 1.5em;
}

.nologolink {
    font-size: 3rem;
    text-decoration: underline;
}

.date {
    color: gray;
    font-style: italic;
}
</style>
