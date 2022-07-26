<template>
 <div>
  <h3>first moon step for Expoverse</h3>

  <canvas></canvas>
 </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { StandardMaterials } from '@/BabylonExamples/StandardMaterials'; 


export default defineComponent({
  name: 'BabylonExamples',
  mounted(){
    const canvas = document.querySelector("canvas")!;
    new StandardMaterials(canvas);
  }
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
canvas{
  width: 80%;
  height: 70%;

}
</style>
