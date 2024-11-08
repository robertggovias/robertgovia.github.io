import * as THREE from 'https://unpkg.com/three@0.127.0/build/three.module.js';

const canvas = document.querySelector('.webgl')
const scene = new THREE.Scene();

const geometry = new THREE.BoxGeometry(1,1,1)
const material = new THREE.MeshBasicMaterial({
    color: 0x00ff00
})

const mesh = THREE.Mesh(geometry, material)
scene.add(mesh)

//Boile plate code

const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}

const camera = new THREE.PerspectiveCamera (75, sizes.width/sizes.height, 0.1, 100)
camera.position.set(0,1,2)
scene.add(camera)

const rendered = new THREE.WebGL1Renderer({
    canvas: canvas
})
rendered.setSize(sizes.width, sizes.height)
rendered.setPixelRatio(Math.min(window.devicePixelRatio,2))
rendered.shadowMap.enabled = true

function animate(){
    requestAnimationFrame(animate)
    rendered.render(scene,camera)
}

animate()