/*---------------------------------------------"
// Template Name: Globe Trekk
// Description:  Globe Trekk Html Template
// Version: 1.0.0

--------------------------------------------*/
var MyScroll = "";
(function (window, document, $, undefined) {
  "use strict";

  var Init = {
    i: function (e) {
      Init.s();
      Init.methods();
    },
    s: function (e) {
      (this._window = $(window)),
        (this._document = $(document)),
        (this._body = $("body")),
        (this._html = $("html"));
    },
    methods: function (e) {
      Init.w();
      Init.preloader();
      Init.gsap();
      Init.searchFunction();
      Init.transitionOnLoad();
      Init.searchToggle();
      Init.wishlistButton();
      Init.niceSelect();
      Init.ionRangeSlider();
      Init.slick();
      Init.videoJS();
      Init.contactForm();
      Init.filterToggle();
    },

    w: function (e) {
      this._window.on("load", Init.l).on("scroll", Init.res);
    },
    // =================
    // Preloader
    // =================
    preloader: function () {
      setTimeout(function () {
        $("#preloader").hide("slow");
      }, 2500);
    },
    // =================
    // Page transitions
    // =================
    transitionOnLoad: function () {

      if($("body").hasClass("ui-transition")) {
  
        // Wait until the whole page is loaded.
        $(window).on("load", function () {
          setTimeout(function () {
            HideLoad(); // call out animations.
          }, 0);
        });

        // Transitions Out (when "ptr-overlay" slides out)
        function HideLoad() {
          var tl_transitOut = gsap.timeline();
      
      
          // ui-Header appear
          // tl_transitOut.from("#ui-header", { duration: 1, y: 20, autoAlpha: 0, ease: Expo.easeInOut, clearProps: "all" }, 0.6);
      
      
          // Page header elements appear (elements with class "ph-appear")
          if ($(".ph-appear").length) {
            tl_transitOut.from(".ph-appear", { duration: 2.0 , y: 60, autoAlpha: 0, stagger: 0.3, ease: Expo.easeOut, clearProps: "all" }, 2.0 );
          }
      
        }
      }
    },
    // =======================
    //  GSAP
    // =======================
    gsap: function () {
      
      gsap.registerPlugin(ScrollTrigger, ScrollSmoother);
      if (window.innerWidth > 1024) {
        MyScroll = ScrollSmoother.create({
          smooth: 0.7,
          effects: true,
          smoothTouch: 1,
        });
        MyScroll.scrollTo(0);
      }
      

      // Banner element scrolling effects:
      // =======================================
      if ($("#hero").hasClass("banner-content-parallax")) {
        let tlPhParallax = gsap.timeline({
          scrollTrigger: {
            trigger: "#hero",
            start: 'top top',
            end: 'bottom top',
            scrub: true,
            markers: false
          }
        });
        
        if ($(".banner-caption-title").length) {
          $(".banner-caption-title").wrapInner('<div class="banner-title-parallax"></div>');
          tlPhParallax.to(".banner-title-parallax", { y: -40 }, 0);
        }
      }

      
      // About 1
      if ($(".about-trigger-1").length ) {
        var sideAnimation1 = gsap.timeline({ default: { ease: "power2.inOut" }, });
        sideAnimation1.to(".about-1 .images-area .v-4", { rotation: 21, duration: 0.3 });
        sideAnimation1.to(".about-1 .images-area .v-3", { x: '0', duration: 0.3 }, '<');
  
        sideAnimation1.to(".about-1 .images-area .v-3", { rotation: 15, duration: 0.3 });
        sideAnimation1.to(".about-1 .images-area .v-2", { x: '0', }, '<')
  
        sideAnimation1.to(".about-1 .images-area .v-2", { rotation: 7, duration: 0.3 });
        sideAnimation1.to(".about-1 .images-area .v-1", { x: '0', duration: 0.3 }, '<')
  
        sideAnimation1.to(".about-1 .images-area .v-1", { rotation: 2, duration: 0.3 });

        ScrollTrigger.create({
          trigger: ".about-trigger-1",
          scrub: true,
          pin: true,
          markers: false,
          start: "top top",
          end: "+=300%",
          animation: sideAnimation1,
        });
      }

      // About 2 
      if ($(".about-trigger-2").length) {
        var sideAnimation3 = gsap.timeline({ default: { ease: "power2.inOut" }, });
        sideAnimation3.to(".about-2 .images-area .v-4", { rotation: -21, duration: 0.3 });
        sideAnimation3.to(".about-2 .images-area .v-3", { x: '0', duration: 0.3 }, '<');
  
        sideAnimation3.to(".about-2 .images-area .v-3", { rotation: -15, duration: 0.3 });
        sideAnimation3.to(".about-2 .images-area .v-2", { x: '0', }, '<')
  
        sideAnimation3.to(".about-2 .images-area .v-2", { rotation: -7, duration: 0.3 });
        sideAnimation3.to(".about-2 .images-area .v-1", { x: '0', duration: 0.3 }, '<')
  
        sideAnimation3.to(".about-2 .images-area .v-1", { rotation: -2, duration: 0.3 });

        ScrollTrigger.create({
          trigger: ".about-trigger-2",
          scrub: true,
          pin: true,
          markers: false,
          start: "top top",
          end: "+=300%",
          animation: sideAnimation3,
        });
      }

      //  Ui Header ================
      
        // Header tools (If ui-Header tools exist)
        if ($(".ui-header-tools").length) {
          $("body").addClass("ui-header-tools-on");

          // Header tools dynamic
          if ($(".ui-header-tools-dynamic").length) {
            $("body").addClass("ui-header-tools-dynamic-on");

            // Move header tools dynamic out of header if the window width is 768px or smaller
            function headerToolsPosition() {
              if (window.matchMedia("(max-width: 768px)").matches) {
                $(".ui-header-tools-dynamic").prependTo("#body-inner");
              } else {
                $(".ui-header-tools-dynamic").prependTo(".ui-header-tools");
              }
            }
            headerToolsPosition();
            $(window).resize(function () {
              headerToolsPosition();
            });
          }
        }
        // On menu toggle button click
        var $olMenuToggleBtn = $(
          ".ui-ol-menu-toggle-btn-text, .ui-ol-menu-toggle-btn"
        );
        $olMenuToggleBtn.on("click", function () {
          $("html").toggleClass("ui-no-scroll");
          $("body").toggleClass("ui-ol-menu-open");
          if ($("body").hasClass("ui-ol-menu-open")) {
            // Menu step in animations
            $("body").addClass("olm-toggle-no-click"); // Disable toggle button click until the animations last.

            var tl_olMenuIn = gsap.timeline({
              onComplete: function () {
                $("body").removeClass("olm-toggle-no-click");
              },
            });

            tl_olMenuIn.to(".ui-overlay-menu", { duration: 0.4, autoAlpha: 1 });
            tl_olMenuIn.from(".ui-ol-menu-list > li", {
              duration: 0.4,
              y: 80,
              autoAlpha: 0,
              stagger: 0.05,
              ease: Power2.easeOut,
              clearProps: "all",
            });

            // On menu link click
            $(".ui-overlay-menu a, .ui-logo a")
              .not('[target="_blank"]') // omit from selection
              .not('[href^="#"]') // omit from selection
              .not('[href^="mailto"]') // omit from selection
              .not('[href^="tel"]') // omit from selection
              .on("click", function () {
                gsap.set("#content-wrap, .ttgr-cat-nav", { autoAlpha: 0 }); // Hide before timeline
                var tl_olMenuClick = gsap.timeline();
                tl_olMenuClick.to(".ui-ol-menu-list > li", {
                  duration: 0.4,
                  y: -80,
                  autoAlpha: 0,
                  stagger: 0.05,
                  ease: Power2.easeIn,
                });
              });

            // Hide sliding sidebar
            if ($(".ui-sliding-sidebar-wrap").length) {
              gsap.to(".ui-sliding-sidebar-trigger", {
                duration: 1,
                autoAlpha: 0,
                ease: Expo.easeOut,
              });
            }
          } else {
            // Menu step out animations
            // =========================
            $("body").addClass("olm-toggle-no-click"); // Disable toggle button click until the animations last.

            var tl_olMenuOut = gsap.timeline({
              onComplete: function () {
                $("body").removeClass("olm-toggle-no-click");
              },
            });
            tl_olMenuOut.to(".ui-ol-menu-list > li", {
              duration: 0.4,
              y: -80,
              autoAlpha: 0,
              stagger: 0.05,
              ease: Power2.easeIn,
            });
            tl_olMenuOut.to(
              ".ui-overlay-menu",
              { duration: 0.4, autoAlpha: 0, clearProps: "all" },
              "+=0.2"
            );
            tl_olMenuOut.set(".ui-ol-menu-list > li", { clearProps: "all" }); // clearProps only

            // Show sliding sidebar
            if ($(".ui-sliding-sidebar-wrap").length) {
              gsap.to(
                ".ui-sliding-sidebar-trigger",
                {
                  duration: 1,
                  autoAlpha: 1,
                  ease: Expo.easeOut,
                  clearProps: "all",
                },
                "-=0.3"
              );
            }

            // Close open submenus
            setTimeout(function () {
              $(".ui-ol-submenu").slideUp(350);
              $(".ui-ol-submenu-trigger").removeClass("ui-ol-submenu-open");
            }, 500);
          }

          return false;
        });
        // Menu list hover
        $(".ui-ol-menu-list")
        .on("mouseenter", function () {
          $(this).addClass("ui-ol-menu-hover");
        })
        .on("mouseleave", function () {
          $(this).removeClass("ui-ol-menu-hover");
        });
        // Open submenu if link href contains #
        $(".ui-ol-submenu-trigger > a").on("click", function () {
          if ($(this).is('[href^="#"]')) {
            var $this = $(this).parent();
            if ($this.hasClass("ui-ol-submenu-open")) {
              $this.removeClass("ui-ol-submenu-open");
              $this.next().slideUp(350);
            } else {
              $this
                .parent()
                .parent()
                .find(".ui-ol-submenu")
                .prev()
                .removeClass("ui-ol-submenu-open");
              $this.parent().parent().find(".ui-ol-submenu").slideUp(350);
              $this.toggleClass("ui-ol-submenu-open");
              $this.next().slideToggle(350);
            }
          }
          return false;
        });
        // Open submenu on caret click
        $(".ui-ol-submenu-caret-wrap").on("click", function () {
          var $this = $(this).parent();
          if ($this.hasClass("ui-ol-submenu-open")) {
            $this.removeClass("ui-ol-submenu-open");
            $this.next().slideUp(350);
          } else {
            $this
              .parent()
              .parent()
              .find(".ui-ol-submenu")
              .prev()
              .removeClass("ui-ol-submenu-open");
            $this.parent().parent().find(".ui-ol-submenu").slideUp(350);
            $this.toggleClass("ui-ol-submenu-open");
            $this.next().slideToggle(350);
          }
        });
        

    },
    // =======================
    //  Search Function
    // =======================
    searchFunction: function () {
      if ($("#searchInput").length) {
        $("#searchInput").on("keyup", function () {
          var value = $(this).val().toLowerCase();
          $(".item-card").filter(function () {
            var hasMatch = $(this).find(".title").text().toLowerCase().indexOf(value) > -1;
            $(this).toggle(hasMatch);
          });
        });
      }
    },
    // =======================
    //  Search Popup
    // =======================
    searchToggle: function () {
      if ($(".search-toggler").length) {
        $(".search-toggler").on("click", function (e) {
          e.preventDefault();
          $(".search-popup").toggleClass("active");
          $(".mobile-nav__wrapper").removeClass("expanded");
          $("body").toggleClass("locked");
        });
      }
    },
    // =======================
    //  Wishlist Button
    // =======================
    wishlistButton: function () {
      if ($(".wishlist-icon").length) {
        $(".wishlist-icon").on("click", function () {
          $(this).find(".fa-light").toggleClass("fa-solid");
          return false;
        });
      }
    },
    // =======================
    //  Nice Select
    // =======================
    niceSelect: function () {
      if ($(".has-nice-select").length) {
        $('.has-nice-select, .contact-form select').niceSelect();
      }
    },
    // =======================
    //  ion Range Slider
    // =======================
    ionRangeSlider: function () {
      if ($(".range-slider").length) {
        $(".range-slider").ionRangeSlider({
          skin: "round",
          type: "double",
          grid: false,
          min: 200,
          max: 3000,
          from: 700,
          to: 2500,
          hide_min_max: false,
          hide_from_to: false,
        });
      }
    },
    // =======================
    //  Slick Slider
    // =======================
    slick: function () {
      if ($(".testimonials-slider").length) {
        $('.testimonials-slider').slick({
          autoplay: false,
          speed: 800,
          lazyLoad: 'progressive',
          arrows: false,
          infinite: true,
          dots: true,
          autoplay: true,
          slidesToShow: 4,
          slidesToScroll: 1,
          responsive: [
            {
              breakpoint: 1399,
              settings: {
                slidesToShow: 3,
              },
            },
            {
              breakpoint: 1199,
              settings: {
                slidesToShow: 2,
              },
            },
            {
              breakpoint: 650,
              settings: {
                slidesToShow: 1,
              },
            },
          ],
        });
      }
      if ($(".blogs-slider").length) {
        $('.blogs-slider').slick({
          autoplay: false,
          speed: 800,
          lazyLoad: 'progressive',
          arrows: false,
          infinite: true,
          dots: true,
          autoplay: true,
          slidesToShow: 4,
          slidesToScroll: 1,
          responsive: [
            {
              breakpoint: 1399,
              settings: {
                slidesToShow: 3,
              },
            },
            {
              breakpoint: 1199,
              settings: {
                slidesToShow: 2,
              },
            },
            {
              breakpoint: 650,
              settings: {
                slidesToShow: 1,
              },
            },
          ],
        });
      }
      if ($(".gallery-slider").length) {
        $(".gallery-slider").slick({
          slidesToShow: 6,
          arrows: false,
          dots: false,
          infinite: true,
          autoplay: true,
          cssEase: "linear",
          autoplaySpeed: 0,
          speed: 6000,
          pauseOnFocus: false,
          pauseOnHover: false,
          responsive: [
            {
              breakpoint: 1399,
              settings: {
                slidesToShow: 5,
              },
            },
            {
              breakpoint: 1199,
              settings: {
                slidesToShow: 4,
              },
            },
            {
              breakpoint: 992,
              settings: {
                slidesToShow: 3,
              },
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 3,
              },
            },
            {
              breakpoint: 492,
              settings: {
                slidesToShow: 2,
              },
            },
            {
              breakpoint: 340,
              settings: {
                slidesToShow: 1,
              },
            },
          ],
        });
      }
    },
    // =======================
    //  Video Js
    // =======================
    videoJS: function () {
      if ($(".bg-video").length) {
        var video = $('#videoPlayer')[0];
        video.play();
      }
    },
    // =======================
    //  Contact Form
    // =======================
    contactForm: function () {
      $(".contact-form").on("submit", function (e) {
        e.preventDefault();
        if ($(".contact-form").valid()) {
          var _self = $(this);
          _self
            .closest("div")
            .find('button[type="submit"]')
            .attr("disabled", "disabled");
          var data = $(this).serialize();
          $.ajax({
            url: "./assets/mail/contact.php",
            type: "post",
            dataType: "json",
            data: data,
            success: function (data) {
              $(".contact-form").trigger("reset");
              _self.find('button[type="submit"]').removeAttr("disabled");
              if (data.success) {
                document.getElementById("message").innerHTML =
                  "<h5 class='text-success mt-3 mb-2'>Email Sent Successfully</h5>";
              } else {
                document.getElementById("message").innerHTML =
                  "<h5 class='text-danger mt-3 mb-2'>There is an error</h5>";
              }
              $("#message").show("slow");
              $("#message").slideDown("slow");
              setTimeout(function () {
                $("#message").slideUp("hide");
                $("#message").hide("slow");
              }, 3000);
            },
          });
        } else {
          return false;
        }
      });
    },
    // =======================
    //  Filter Toggle
    // =======================
    filterToggle: function () {
      if ($('.sidebar-widget').length) {
        $(".widget-title-row").on("click", function (e) {
          $(this).find('i').toggleClass('fa-horizontal-rule fa-plus', 'slow');
          // $(this).find('i').toggleClass('fa-light fa-regular', 'slow');
          $(this).parents('.sidebar-widget').find('.widget-content-block').animate({ height : 'toggle'}, 'slow');
        })
      }
    },
  };

  Init.i();
})(window, document, jQuery);