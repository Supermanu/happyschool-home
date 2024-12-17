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
            no-body
            class="mb-1"
        >
            <BListGroup flush>
                <BListGroupItem>
                    <strong>Derniers messages</strong>
                    <BButton
                        size="sm"
                        variant="outline-primary"
                        class="ms-1"
                        v-b-toggle.searchemails
                    >
                        <IBiSearch />
                    </BButton>
                </BListGroupItem>
                <BCollapse id="searchemails">
                    <BListGroupItem>
                        <BInputGroup>
                            <template #prepend>
                                <BInputGroupText>
                                    <IBiSearch />
                                </BInputGroupText>
                            </template>
                            <BFormInput
                                v-model="search"
                                @input="getEmails"
                                placeholder="Rechercher un courriel"
                            />
                        </BInputGroup>
                    </BListGroupItem>
                </BCollapse>
                <BPlaceholderWrapper :loading="loading">
                    <template #loading>
                        <BListGroupItem>
                            <BPlaceholder width="70%" />
                        </BListGroupItem>
                        <BListGroupItem>
                            <BPlaceholder width="30%" />
                        </BListGroupItem>
                        <BListGroupItem>
                            <BPlaceholder width="50%" />
                        </BListGroupItem>
                        <BListGroupItem>
                            <BPlaceholder width="80%" />
                        </BListGroupItem>
                        <BListGroupItem>
                            <BPlaceholder width="70%" />
                        </BListGroupItem>
                    </template>
                    <BListGroupItem
                        v-for="email in emails"
                        :key="email.id"
                        :to="`/email/${email.id}/`"
                        v-b-tooltip.hover="email.datetime_created.slice(0, 10)"
                    >
                        {{ email.subject }}
                    </BListGroupItem>
                </BPlaceholderWrapper>
                <BListGroupItem>
                    <BPagination
                        v-model="currentPage"
                        :total-rows="emailCount"
                        per-page="5"
                    />
                </BListGroupItem>
            </BListGroup>
        </BCard>
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
            emailCount: 0,
            search: "",
            searchId: -1,
        };
    },
    watch: {
        currentPage: function () {
            this.getEmails();
        },
    },
    methods: {
        getEmails: function () {
            this.loading = true;
            this.searchId += 1;
            const currentSearch = this.searchId;
            axios.get(`/mail_notification/api/notif/?page_size=5&page=${this.currentPage}&search=${this.search}`)
                .then(resp => {
                    if (this.searchId !== currentSearch)
                        return;
                    this.emails = resp.data.results;
                    this.emailCount = resp.data.count;
                    this.loading = false;
                })
                .catch(err => {
                    this.loading = false;
                    console.log(err);
                });
        }
    },
    mounted: function () {
        this.getEmails();
    }
};
</script>
