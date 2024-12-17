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
    <BContainer>
        <BRow class="mt-2">
            <BCol>
                <BButton to="/">
                    Retour
                </BButton>
            </BCol>
        </BRow>
        <BRow>
            <BCol>
                <BCard
                    v-if="email"
                    :title="email.subject"
                    :sub-title="email.datetime_created.slice(0, 10)"
                    class="mt-2"
                >
                    <BCardBody>
                        <span v-html="email.body" />
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
    </BContainer>
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
