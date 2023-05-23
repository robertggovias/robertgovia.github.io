// Load the GLB file
const loader = new GLTFLoader();
loader.load('path/to/model.glb', (gltf) => {
  // Get the mesh from the GLTF object
  const mesh = gltf.scene.children[0];

  // Create a convex hull shape for the mesh
  const geometry = new ConvexGeometry(mesh.geometry.vertices);
  const cannonShape = new Cannon.ConvexPolyhedron(geometry.vertices, geometry.faces);

  // Create a Cannon.js body for the mesh
  const mass = 0;
  const body = new Cannon.Body({ mass, shape: cannonShape });

  // Set the initial position of the body
  body.position.copy(mesh.position);
  body.quaternion.copy(mesh.quaternion);

  // Add the body to the Cannon.js world
  world.addBody(body);

  // Add the mesh to the Three.js scene
  scene.add(mesh);

  // Animate the scene
  function animate() {
    requestAnimationFrame(animate);

    // Update the Cannon.js physics simulation
    world.step(timeStep);

    // Update the position and rotation of the mesh to match the Cannon.js body
    mesh.position.copy(body.position);
    mesh.quaternion.copy(body.quaternion);

    // Update the Three.js renderer
    renderer.render(scene, camera);
  }

  // Start the animation loop
  animate();
});