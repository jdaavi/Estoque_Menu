const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
      nav = document.getElementById(navId);
  
    toggle.addEventListener("click", () => {
      nav.classList.toggle("show-menu");
      toggle.classList.toggle("show-icon");
    });
  };
  

  <script>
    function handleSair() {
      document.querySelector('.sidebar').classList.add('fade-out');

      setTimeout(function() {
        window.location.href = "/inicio"
    }, 500); 
  }
  </script>

  showMenu("nav-toggle", "nav-menu");

