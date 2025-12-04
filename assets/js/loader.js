async function loadManifest() {
  const r = await fetch('posts/posts.json');
  const posts = await r.json();
  const list = document.getElementById('post-list');
  posts.forEach(p => {
    const li = document.createElement('li');
    li.textContent = p;
    li.onclick = ()=> loadPost(p);
    list.appendChild(li);
  });
  loadPost(posts[0]);
}
async function loadPost(p){
  history.pushState({}, '', '?post=' + p.split('/')[1].replace('.html',''));
  const r = await fetch(p);
  const html = await r.text();
  document.getElementById('content').innerHTML = html;
}
window.onload = loadManifest;
