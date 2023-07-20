js_do_everything = """
        async (images_selected_state, multi_select_ckbx_state) => {
          const gallery = document.querySelector("#gallery_id")
          const buttons_thumbnails = gallery.querySelectorAll(".thumbnails > button");
          const buttons_large = gallery.querySelectorAll(".grid-container > button");
          buttons_thumbnails.forEach((btn, idx) => {
            if(images_selected_state.includes(idx)){
              btn.classList.add('selected-custom');
            }else{
              btn.classList.remove('selected-custom');
            }
            btn.classList.remove('selected');
          })
          buttons_large.forEach((btn, idx) => {
            if(images_selected_state.includes(idx)){
              btn.classList.add('selected-custom');
            }else{
              btn.classList.remove('selected-custom');
            }
          })
          const elements = document.querySelectorAll('*[class^="preview"], *[class*=" preview"]');
          elements.forEach(element => {
            if (multi_select_ckbx_state[0]) {
              element.style.display = 'none';
            } else {
              element.style.display = '';
              element.style.removeProperty('display');
            }
          })
          return images_selected_state
        }
        """

js_set_colors_on_list_required = """
        async (tags, categories) => {
          // I'm assuming you have a mapping from categories to colors
          let categoryToColor = {
            "artist": "yellow",
            "character": "green",
            "species": "red",
            "general": "white",
            "rating": "cyan",
            "meta": "purple",
            "invalid": "black",
            "lore": "black",
            "copyright": "violet"
          };

          const gallery = document.querySelector("#required_dropdown");
          const ulElements = gallery.querySelectorAll("ul");

          for(let ul of ulElements) {
            let liElements = ul.querySelectorAll("li");
            // If there are <li> elements, we add the class
            liElements.forEach(li => {
              let tagIndex = tags.indexOf(li.getAttribute('data-value'));
              if(tagIndex !== -1) {
                li.style.color = categoryToColor[categories[tagIndex]];
              }
            });
          }
        }
        """

js_set_colors_on_list_blacklist = """
        async (tags, categories) => {
          // I'm assuming you have a mapping from categories to colors
          let categoryToColor = {
            "artist": "yellow",
            "character": "green",
            "species": "red",
            "general": "white",
            "rating": "cyan",
            "meta": "purple",
            "invalid": "black",
            "lore": "black",
            "copyright": "violet"
          };

          const gallery = document.querySelector("#blacklist_dropdown");
          const ulElements = gallery.querySelectorAll("ul");

          for(let ul of ulElements) {
            let liElements = ul.querySelectorAll("li");
            // If there are <li> elements, we add the class
            liElements.forEach(li => {
              let tagIndex = tags.indexOf(li.getAttribute('data-value'));
              if(tagIndex !== -1) {
                li.style.color = categoryToColor[categories[tagIndex]];
              }
            });
          }
        }
        """

js_set_colors_on_list_add_tag = """
        async (tags, categories) => {
          // I'm assuming you have a mapping from categories to colors
          let categoryToColor = {
            "artist": "yellow",
            "character": "green",
            "species": "red",
            "general": "white",
            "rating": "cyan",
            "meta": "purple",
            "invalid": "black",
            "lore": "black",
            "copyright": "violet"
          };

          const gallery = document.querySelector("#add_tag_dropdown");
          const ulElements = gallery.querySelectorAll("ul");

          for(let ul of ulElements) {
            let liElements = ul.querySelectorAll("li");
            // If there are <li> elements, we add the class
            liElements.forEach(li => {
              let tagIndex = tags.indexOf(li.getAttribute('data-value'));
              if(tagIndex !== -1) {
                li.style.color = categoryToColor[categories[tagIndex]];
              }
            });
          }
        }
        """

js_set_colors_on_list_searchbar = """
        async (tags, categories) => {
          // I'm assuming you have a mapping from categories to colors
          let categoryToColor = {
            "artist": "yellow",
            "character": "green",
            "species": "red",
            "general": "white",
            "rating": "cyan",
            "meta": "purple",
            "invalid": "black",
            "lore": "black",
            "copyright": "violet"
          };

          const gallery = document.querySelector("#searchbar_dropdown");
          const ulElements = gallery.querySelectorAll("ul");

          for(let ul of ulElements) {
            let liElements = ul.querySelectorAll("li");
            // If there are <li> elements, we add the class
            liElements.forEach(li => {
              let tagIndex = tags.indexOf(li.getAttribute('data-value'));
              if(tagIndex !== -1) {
                li.style.color = categoryToColor[categories[tagIndex]];
              }
            });
          }
        }
        """
