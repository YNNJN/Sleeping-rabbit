<template>
  <div>
    <h1 class="bold mb-5 text-center">Movie List</h1>
    <div class="p-4"></div>
    <div class="movieList row">
      <MovieListItem
        :movie="movie"
        v-for="movie in movies.slice(0,8)"
        :key="movie.DOCID"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  props: {
    movies: Array,
  },
  methods: {

  },
}
</script>

<style>
.bold {
  color: #d8dcff;
  background-color: #1c1c38;
  border-radius: 0.5rem;
  width: 44rem;
  margin: auto;
  font-family: 'NeoDunggeunmo';
  font-weight: bold;
  font-style: normal;
}
</style>