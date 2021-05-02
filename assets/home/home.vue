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
                <b-col>
                    <h1>Bienvenue sur HappySchool</h1>
                </b-col>
            </b-row>
            <b-row>
                <b-col
                    cols="12"
                    md="6"
                >
                    <div class="text-center">
                        <h3>Vers les autres plateformes</h3>
                        <a
                            href="https://eplateforme.isln.be/"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                src="/static/img/logo_moodle.png"
                                alt="Moodle logo"
                            >
                        </a>
                        <a
                            href="https://grr.isln.be/"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                src="/static/img/logo_grr.png"
                                alt="GRR logo"
                            >
                        </a>
                        <a
                            href="https://isln.it-school.be/"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                width="320"
                                src="https://isln.it-school.be/bundles/itschoolwebadmin/itschool/media/logo-it-school.png"
                                alt="GRR logo"
                            >
                        </a>
                        <a
                            href="https://ajax.webuntis.com/WebUntis/?school=Institut+Saint-Louis#/basic/login"
                            target="_blank"
                            rel="noreferrer noopener"
                        >
                            <img
                                src="/static/img/logo_untis.png"
                                alt="WebUntis logo"
                            >
                        </a>
                    </div>
                </b-col>
                <b-col>
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
                    <b-card no-body>
                        <b-card-body>
                            <b-icon
                                icon="question-circle"
                                class="question"
                                variant="primary"
                            />
                            Quelles sont les plateformes utilisées ?
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
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

export default {
    data: function () {
        return {
        };
    },
};
</script>

<style>
.question {
    width: 1.5em;
    height: 1.5em;
}
</style>
