<template>
    <b-container>
        <b-row>
            <b-col>
                <b-btn to="/">
                    Retour
                </b-btn>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <b-overloay :show="loading">
                    <b-card
                        :title="email.subject"
                        :sub-title="email.datetime_created.slice(0, 10)"
                        class="mt-2"
                    >
                        <b-card-body>
                            <span v-html="email.body" />
                        </b-card-body>
                    </b-card>
                </b-overloay>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import axios from "axios";

export default {
    props: {
        id: {
            type: String,
            default: "-1"
        }
    },
    data: function () {
        return {
            email: null,
            loading: true,
        };
    },
    mounted: function () {
        this.loading = true;
        axios.get(`/mail_notification/api/notif/${this.id}`)
            .then(resp => {
                this.email = resp.data;
                this.loading = false;
            });
    }
};
</script>

<style>
</style>
