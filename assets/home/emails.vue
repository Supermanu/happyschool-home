<template>
    <div>
        <b-card
            no-body
            class="mb-1"
        >
            <b-list-group flush>
                <b-list-group-item>
                    <strong>Derniers messages</strong>
                </b-list-group-item>
                <b-skeleton-wrapper :loading="loading">
                    <template #loading>
                        <b-list-group-item>
                            <b-skeleton width="70%" />
                        </b-list-group-item>
                        <b-list-group-item>
                            <b-skeleton width="30%" />
                        </b-list-group-item>
                        <b-list-group-item>
                            <b-skeleton width="50%" />
                        </b-list-group-item>
                        <b-list-group-item>
                            <b-skeleton width="80%" />
                        </b-list-group-item>
                        <b-list-group-item>
                            <b-skeleton width="70%" />
                        </b-list-group-item>
                    </template>
                    <b-list-group-item
                        v-for="email in emails"
                        :key="email.id"
                        :to="`/email/${email.id}/`"
                        v-b-tooltip.hover
                        :title="email.datetime_created.slice(0, 10)"
                    >
                        {{ email.subject }}
                    </b-list-group-item>
                </b-skeleton-wrapper>
                <b-list-group-item>
                    <b-pagination
                        v-model="currentPage"
                        :total-rows="emailCount"
                        per-page="5"
                    />
                </b-list-group-item>
            </b-list-group>
        </b-card>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data: function () {
        return {
            loading: true,
            emails: [],
            currentPage: 1,
            emailCount: 0
        };
    },
    watch: {
        currentPage: function () {
            this.getEmails();
        }
    },
    methods: {
        getEmails: function () {
            this.loading = true;
            axios.get(`/mail_notification/api/notif/?page_size=5&page=${this.currentPage}`)
                .then(resp => {
                    this.emails = resp.data.results;
                    this.emailCount = resp.data.count;
                    this.loading = false;
                })
                .catch(err => {
                    this.loading = false;
                    console.log(err);
                })
        }
    },
    mounted: function () {
        this.getEmails();
    }
};
</script>
