<template>
  <div class="container">
    <div class="stage">
      <div class="character turtle"><img src="@/assets/turtle.png" width="80%"></div>
      <div class="character rabbit_walking"><img src="@/assets/rabbit_walking.png" width="75%"></div>
    </div>
    <div class="p-5">
      <v-card>
        <v-card-text>
          <v-slider @mousedown="onPoint(value)" v-model="value" label="How long?" :min="0" :max="140" append-icon="alarm" thumb-label ticks></v-slider>
        </v-card-text>
      </v-card>
      <div class="container mt-5 p-0">
        <div class="row p-0 m-0" v-if="show_on == true">
          <div v-for="ele in movie" :key="ele.DOCID" class="col-md-3 p-0">
            <div class="card_form card text-center p-2 border-0">
              <p class="card-title text-secondary"> {{ ele.title }}</p>
              <img :src="ele.posters" class="card-img-top" :alt="ele.title">
              <p class="badge badge-light">⏱{{ ele.runtime }}분</p>
              <div class="card-body">
                <button class="detail_button btn btn-secondary" data-toggle="modal" :data-target="'#movie'+ele.DOCID">자세히보기</button>
              </div>
            </div>
            <PickMovieDetail :ele="ele"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PickMovieDetail from './PickMovieDetail.vue'

const USER_API_URL = 'http://127.0.0.1:8000/accounts/user_info/'

export default {
  name: 'PickItem',
  components: {
    PickMovieDetail
  },
  props: {
    movies: {
      type: Array,
      required: true,
    },
  },
  data(){
    return {
      movie: [],
      show_on: false,
      user_info: Object,
    }
  },
  methods: {
    onPoint(value) {
      this.movies.forEach(temp_movie => {
        if (temp_movie.runtime === value) {
          if (this.user_info.age < 19) {
            if (temp_movie.rating.slice(0,2) != 18 && temp_movie.rating.slice(0,2) != "") {
              // console.log(temp_movie.rating.slice(0,2))
              return this.movie.push(temp_movie)
            } 
          }
          else if (this.user_info.age > 19) {
            return this.movie.push(temp_movie)
          }
        }
      })
      this.value = ''
      this.show_on = true
    },
  },
  computed: {

  },
  created() {
    // get my information
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get('auth-token')}`
      },
    }
    axios.get(USER_API_URL, config)
    .then(res => {
      this.user_info = res.data
      // console.log(this.user_info.age)
    })
    .catch(err => console.log(err))
  },
}
</script>

<style scoped>
.card {
  background-color: #d8dcff;
  border-radius: 0.8rem;
}

.PickMovieDetail {
  background-color: #d8dcff;
  border-radius: 0.8rem;
}

.stage {
  position: relative;
  width: 80vw;
  height: 4vh;
}

@keyframes moving {
  from {
    transform: translateX(90vw);
  }
  to {
    transform: translateX(0);
  }
}

.character {
position: absolute;
  width: 150px;
  height: 100px;
  background-repeat: no-repeat;
  background-position: 50% 50%;
  background-size: contain;
  animation: moving infinite alternate;
}

.character.turtle {
  left: 5%;
  bottom: 35%;
  animation-duration: 25s;
  z-index: 1;
}

.character.rabbit_walking {
  left: 10%;
  bottom: 10%;
  animation-duration: 7s;
}

</style>