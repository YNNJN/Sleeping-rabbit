<template>
  <div class="home">
    <span class="slogan">마감에 쫓기는 완벽주의자를 위한 영화와 함께 쉬어가기 프로젝트</span>
    <div class="p-5">
      <div class="d-flex justify-content-center">
        <div class="thirty text-center m-2">
          <div @click="get30data()" type="button" class="btn text-dark" data-toggle="modal" data-target="#minuteModal">
            <p style="font-size:2.5rem">30 min</p>
            <img class="rabbit_icon" src="@/assets/rabbit_sleeping.png">
          </div>
        </div>
        <div class="sixty text-center m-2">
          <div @click="get60data()" type="button" class="btn text-dark" data-toggle="modal" data-target="#hourModal">
            <p style="font-size:2.5rem">60 min</p>
            <img class="turtle_icon" src="@/assets/turtle.png">
          </div>
        </div>
      </div>
    </div>

    <!-- modal -->
    <div class="modal fade bd-example-modal-lg" id="minuteModal" tabindex="-1" role="dialog" aria-labelledby="minuteModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="minuteModalLabel">30분 분량의 영화를 만나보세요</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="row modal-body">
            <div v-for=" movie in movie_thirty" :key="movie.DOCID" class="abstract text-left">
              <p class="title_tag"><strong>영화명: {{ movie.title }}</strong></p>
              <div class="p-0">
                <p class="badge badge-success text-white">{{ movie.genre }} {{ movie.rating }}</p>
                <p v-if="movie.directorNm.length"><strong>감독명:</strong> {{ movie.directorNm }}</p>
                <p v-if="movie.keywords.length"><strong>키워드:</strong> {{ movie.keywords }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade bd-example-modal-lg" id="hourModal" tabindex="-1" role="dialog" aria-labelledby="hourModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="hourModalLabel">60분 분량의 영화를 만나보세요</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="row modal-body">
            <div v-for=" movie in movie_sixty" :key="movie.DOCID" class="abstract text-left">
              <p class="title_tag"><strong>영화명: {{ movie.title }}</strong></p>
              <div class="p-0">
                <p class="badge badge-success text-white">{{ movie.genre }} {{ movie.rating }}</p>
                <p v-if="movie.directorNm.length"><strong>감독명:</strong> {{ movie.directorNm }}</p>
                <p v-if="movie.keywords.length"><strong>키워드:</strong> {{ movie.keywords }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div class="p-3">
      <p class="lead text-center mt-5">가장 빠른 영화를 이곳에서 만나세요 !</p>
      <button v-if="showButton" @click="getMovieData" class="start_button btn"><strong>start</strong></button>
    </div>
    <div class="container mt-5 p-0">
      <MovieList :movies="movies"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/movies/MovieList.vue'

const MOIVE_API_URL = 'http://127.0.0.1:8000/movies/'
export default {
  name: 'Home',
  components: {
    MovieList,
  },

  data() {
    return {
      movies: [],
      movielist: [],
      showButton: true,
      movie_sixty: [],
      movie_thirty: [],
    }
  },
  methods: {
    getMovieData() {
      this.showButton = false
      axios.get(MOIVE_API_URL)
      .then(res => {
        this.movies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    get30data() {
      axios.get(MOIVE_API_URL)
      .then(res => {
        this.movielist = res.data
        this.movielist.forEach(temp_movie => {
          if (temp_movie.runtime === 30) {
            return this.movie_thirty.push(temp_movie)
          }
        })
      })
    },
    get60data() {
      axios.get(MOIVE_API_URL)
      .then(res => {
        this.movielist = res.data
        this.movielist.forEach(temp_movie => {
          if (temp_movie.runtime === 60) {
            return this.movie_sixty.push(temp_movie)
          }
        })
      })
    },
  },
}
</script>
<style>
.home {
  text-align: center;
}

.slogan {
  color: #5d4c5f;
  background-color: paleturquoise;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

.lead {
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}

.thirty {
  height: 20rem;
  width: 20rem;
  background-color: slategrey;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
  transition: 0.5s;
}

.thirty:hover {
  transform: scale(1.2) rotate(-10deg);
  opacity: 0.9;
}

.sixty {
  height: 20rem;
  width: 20rem;
  background-color: seagreen;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
  transition: 0.5s;
}

.sixty:hover {
  transform: scale(1.2) rotate(10deg);
  opacity: 0.9;
}

.rabbit_icon {
  margin-top: 1.5rem;
  width: 150px;
  height: 225px;
}

.turtle_icon {
  width: 160px;
  height: 240px;
}

.start_button {
  display: block;
  background-color: #d8dcff;
  font-size: 1.2rem;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
  margin: auto;
}

.abstract {
  background-color: #f5f5f5;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  margin: 1rem;
  width: 350px;
}

.title_tag {
  background-color: paleturquoise;
  border-radius: 1rem;
  width: 15rem;
  font-family: 'NeoDunggeunmo';
  font-weight: normal;
  font-style: normal;
}
</style>