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
        <b-container>
            <b-row>
                <b-col
                    cols="12"
                    md="8"
                >
                    <b-row>
                        <birthdays people="responsible" />
                        <birthdays
                            people="student"
                            :teaching="teaching"
                        />
                    </b-row>
                    <b-row>
                        <b-col>
                            <b-btn
                                v-if="$store.state.canAddNews"
                                variant="success"
                                v-b-modal.new-new
                                class="mb-1"
                            >
                                <b-icon icon="plus" />
                                Ajouter une nouvelle
                            </b-btn>
                        </b-col>
                    </b-row>
                    <b-overlay :show="loadingNews">
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
                    </b-overlay>
                </b-col>
                <b-col
                    cols="12"
                    md="4"
                >
                    <emails />
                    <b-card
                        no-body
                        class="mb-2"
                    >
                        <b-card-body>
                            <b-icon
                                icon="question-circle"
                                class="question"
                                variant="primary"
                            />
                            Comment s'y retrouver dans l'organisation de l'école ?
                            <br>
                            <a
                                href="https://view.genial.ly/60655e69ccc9790cde59cada/presentation-isln-organigramme"
                                target="_blank"
                                rel="noreferrer noopener"
                            >
                                <b-icon icon="link45deg" />Organigramme de l'Institut Saint-Louis
                            </a>
                        </b-card-body>
                    </b-card>
                    <b-card
                        no-body
                        class="mb-2"
                    >
                        <b-card-body>
                            <b-icon
                                icon="question-circle"
                                class="question"
                                variant="primary"
                            />
                            Plateformes : À qui s'adresser en cas de besoin ?
                            <br>
                            <a
                                href="https://view.genial.ly/5ffdaf1608ab8e3755b3b9b9/presentation-isln-plateformes"
                                target="_blank"
                                rel="noreferrer noopener"
                            >
                                <b-icon icon="link45deg" />Les plateformes numériques à l'Institut Saint-Louis
                            </a>
                        </b-card-body>
                    </b-card>
                    <b-card no-body>
                        <b-card-body>
                            <b-icon
                                icon="question-circle"
                                class="question"
                                variant="primary"
                            />
                            <a
                                href="https://view.genial.ly/60ef039c01f7650d996dfa9f/presentation-isln-differents-organes-de-lecole"
                                target="_blank"
                                rel="noreferrer noopener"
                            >
                                <b-icon icon="link45deg" />Les différents organes de l'école
                            </a>
                        </b-card-body>
                    </b-card>
                </b-col>
            </b-row>
            <b-row class="text-center">
                <b-col
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
                                src="/static/img/logo_moodle.png"
                                alt="Moodle logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </b-col>
                <b-col
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
                                src="/static/img/logo_bulrezo.png"
                                alt="bulrézo logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </b-col>
                <b-col
                    cols="12"
                    md="3"
                >
                    <div class="px-5 px-md-0">
                        <a
                            href="https://ajax.webuntis.com/WebUntis/?school=Institut+Saint-Louis#/basic/login"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                src="/static/img/logo_untis.png"
                                alt="WebUntis logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </b-col>
                <b-col
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
                                src="/static/img/logo_it-school.png"
                                alt="it-school logo"
                                class="w-100"
                            >
                        </a>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap-vue/dist/bootstrap-vue.css";

import axios from "axios";

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

import News from "./news.vue";
import Birthdays from "./birthday.vue";
import Emails from "./emails.vue";

const token = { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken"};

export default {
    data: function () {
        return {
            news: [],
            loadingNews: false,
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
        }
    },
    methods: {
        updateNews: function (newsIndex, data) {
            this.news.splice(newsIndex, 1, data);
        },
        createNews: function () {
            this.getNews();
        },
        removeNews: function (newsIndex) {
            this.$bvModal.msgBoxConfirm("Êtes-vous sûr de vouloir supprimer cette nouvelle ?", {
                title: "Confirmation",
                size: "sm",
                buttonSize: "sm",
                okVariant: "danger",
                okTitle: "Oui",
                cancelTitle: "Non",
                footerClass: "p-2",
                hideHeaderClose: false,
                centered: true
            })
                .then(resp => {
                    if (resp) {
                        axios.delete(`/home/api/news/${this.news[newsIndex].id}/`, token)
                            .then(() => {
                                this.getNews();
                            })
                            .catch(err => {
                                console.log(err);
                            });
                    }
                })
                .catch(err => {
                    console.log(err);
                });
        },
        getNews: function () {
            this.loadingNews = true;
            axios.get("/home/api/news/")
                .then(resp => {
                    this.loadingNews = false;
                    this.news = resp.data.results;
                })
                .catch(err => {
                    console.log(err);
                    this.loadingNews = false;
                });
        }
    },
    mounted: function () {
        this.getNews();
    },
    components: {
        News,
        Birthdays,
        Emails
    }
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
</style>
