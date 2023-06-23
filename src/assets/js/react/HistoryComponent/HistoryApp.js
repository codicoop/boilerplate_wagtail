import React, { useEffect, useState } from 'react';
import SyncLoader from "react-spinners/SyncLoader"
import axios from 'axios';

export default function HistoryApp(){
  const [allSlides, setAllSlides] = useState([])
  const [currentSlide, setCurrentSlide] = useState("")
  const [loading, setLoading] = useState(true)
  let currentPage

  useEffect(()=>{
    // Agafem la pàgina on som
    const thisApp = document.getElementById("mySliderApp")
    currentPage = thisApp.dataset.page
    console.log("currentPage", currentPage);
  },[])

  useEffect(()=>{
    // Getting the history items
    axios({
      method: 'get',
      url: `/custom_api/history_items/?page=${currentPage}`,
      headers: {'X-CSRFToken': backData.csrf}
    })
    .then(response => {
      setAllSlides(response.data)
      setCurrentSlide(0)
      setLoading(false)
    })
    },[])

    if (loading) {
      return (
        <div className="slider grid-2">
          <div className="slider__loader grid-item-full">
            <SyncLoader
              color="#303030"
              loading={loading}
              data-testid="loader"
            />
          </div>
        </div>
      )
    } else {
      return (
        <div className="history grid-3">
          <div className="history__controller">
            <div className="history__arrow" onClick={handlePreviousSlideChange}>
              <svg viewBox="0 0 11 18" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.26667 17.0522L-4.97667e-06 8.52611L8.26667 -1.92546e-05L10.3385 2.13151L4.13333 8.52611L10.3385 14.9207L8.26667 17.0522Z" />
              </svg>
            </div>
            <div className='history__controller-title'>
              <p>{allSlides[currentSlide].year}</p>
            </div>
            <div className="history__arrow" onClick={handleNextSlideChange}>
              <svg viewBox="0 0 11 18" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.07184 0L10.3385 8.52613L2.07184 17.0523L0 14.9207L6.20517 8.52613L0 2.13153L2.07184 0Z" />
              </svg>
            </div>
          </div>
          <div className="history__photo"
            style={{"backgroundImage": `url(${allSlides[currentSlide].image_maximized.url})`}}
          ></div>
          <div className="history__title title-2">
            <p>{allSlides[currentSlide].title}</p>
          </div>
          <div className="history__text">
            <p>{allSlides[currentSlide].description}</p> 
          </div>
          <div className="history__image">
            <svg viewBox="0 0 477 459" xmlns="http://www.w3.org/2000/svg">
              <path d="M314.26 94.0428C334.59 102.32 338.041 108.07 347.679 117.058C371.1 138.883 366.203 135.925 373.5 146.532C391.446 172.629 391.795 176.705 396.121 190.509C401.239 206.823 401.258 219.404 399.005 236.36C394.978 266.716 392.426 272.15 380.108 300.457C375.413 311.245 367.263 320.026 359.416 328.368C341.388 347.541 324.839 362.226 299.958 370.408C288.572 374.148 270.591 375.972 258.524 377.231C240.801 379.052 237.408 379.938 204.705 374.168C192.991 372.123 181.315 365.338 162.453 358.795C148.051 353.799 136.313 343.798 126.506 333.486C97.3545 302.839 94.2658 291.562 80.1346 250.736C74.1387 233.432 75.2624 214.095 80.1702 196.245C85.781 175.842 88.5308 166.462 96.6053 152.381C116.491 117.7 129.274 113.686 155.06 95.2383C171.321 83.6104 192.336 79.9187 212.391 76.3052C234.979 72.2346 243.785 72.3249 259.048 76.3553C287.133 83.756 295.686 86.4852 314.26 94.0428Z" />
              <path d="M74.6454 160.98C82.4923 138.214 88.9522 133.916 98.6488 122.617C122.193 95.1609 119.164 100.741 130.994 91.807C160.097 69.8312 164.875 69.0473 180.758 62.9992C199.528 55.8449 214.376 54.5664 234.601 55.3014C270.809 56.6114 277.463 58.8227 312.038 69.2835C325.214 73.2718 336.349 81.1877 346.936 88.8207C371.27 106.358 390.166 122.747 402.175 148.778C407.666 160.69 411.52 179.91 414.146 192.806C417.972 211.749 419.338 215.321 415.621 251.188C414.315 264.032 407.41 277.31 401.472 298.318C396.937 314.359 386.243 328.025 375 339.639C341.586 374.16 328.569 378.621 281.72 397.952C261.864 406.153 238.936 406.874 217.404 403.363C192.793 399.349 181.463 397.319 164.079 390.014C121.267 372.024 115.321 358.631 91.11 332.651C75.8488 316.267 69.5045 293.959 63.3433 272.679C56.4032 248.712 55.677 239.2 58.9906 222.327C65.0696 191.281 67.4819 181.779 74.6454 160.98Z" />
              <path d="M193.106 275.829C184.88 269.35 184.072 266.265 180.858 260.88C173.045 247.801 174.896 249.802 172.978 243.987C168.261 229.682 168.653 227.773 168.533 220.892C168.39 212.759 170.085 207.007 173.417 199.558C179.38 186.221 181.29 184.077 190.787 172.776C194.407 168.469 199.344 165.538 204.081 162.767C214.967 156.397 224.565 151.882 237.113 151.444C242.855 151.245 251.369 152.796 257.088 153.822C265.483 155.341 267.163 155.386 281.418 162.36C286.527 164.848 290.976 169.497 298.762 174.989C304.708 179.182 308.75 185.309 311.862 191.322C321.115 209.192 321.008 214.755 321.976 235.284C322.389 243.986 319.253 252.673 314.579 260.179C309.236 268.758 306.701 272.679 301.081 278.042C287.241 291.252 280.82 291.39 266.465 296.399C257.414 299.556 247.252 298.455 237.541 297.446C226.604 296.31 222.568 295.101 216.096 291.235C204.185 284.128 200.623 281.746 193.106 275.829Z"/>
              <path className={currentSlide.id === 1 ? "is-active" : null} d="M233.121 177.697C239.71 175.289 241.845 175.908 246.154 175.965C256.62 176.1 254.807 176.452 258.958 177.396C269.171 179.718 270.204 180.608 274.423 182.946C279.41 185.709 282.357 188.683 285.807 193.181C291.986 201.233 292.672 203.068 296.473 212.415C297.922 215.978 298.11 219.808 298.265 223.468C298.622 231.881 298.269 238.912 294.486 246.195C292.755 249.527 289.065 253.822 286.597 256.712C282.966 260.951 282.397 261.889 273.561 267.55C270.401 269.582 266.141 270.484 260.293 272.988C255.827 274.899 250.801 275.053 246.144 274.719C232.303 273.727 228.958 271.721 216.174 265.092C210.755 262.284 206.489 257.464 203.437 252.184C199.95 246.149 198.385 243.337 196.94 238.269C193.381 225.786 195.368 222.09 196.956 212.183C197.959 205.937 201.906 200.548 205.652 195.383C209.871 189.567 211.908 187.696 216.344 185.371C224.505 181.09 227.101 179.898 233.121 177.697Z" />
              <path className={currentSlide.id === 0 ? "is-active" : null} d="M238.57 196.735C242.788 195.205 244.148 195.584 246.9 195.604C253.582 195.65 252.423 195.877 255.071 196.451C261.582 197.866 262.239 198.419 264.923 199.866C268.097 201.575 269.967 203.425 272.152 206.225C276.064 211.238 276.495 212.383 278.885 218.215C279.795 220.438 279.9 222.833 279.984 225.121C280.178 230.381 279.924 234.78 277.479 239.349C276.36 241.439 273.987 244.139 272.399 245.956C270.063 248.62 269.695 249.209 264.03 252.782C262.004 254.065 259.28 254.645 255.535 256.232C252.676 257.444 249.466 257.559 246.493 257.367C237.659 256.798 235.531 255.555 227.394 251.457C223.945 249.72 221.24 246.722 219.313 243.431C217.11 239.669 216.123 237.916 215.22 234.752C212.998 226.958 214.282 224.639 215.336 218.437C216.002 214.527 218.544 211.142 220.957 207.898C223.675 204.245 224.983 203.067 227.826 201.597C233.054 198.889 234.717 198.134 238.57 196.735Z" />
              <path d="M242.832 210.268C244.939 209.504 245.619 209.694 246.993 209.704C250.331 209.726 249.752 209.84 251.075 210.127C254.328 210.833 254.655 211.11 255.996 211.832C257.582 212.686 258.516 213.61 259.607 215.009C261.562 217.513 261.777 218.085 262.971 220.998C263.426 222.109 263.478 223.305 263.52 224.448C263.617 227.076 263.49 229.273 262.269 231.556C261.71 232.6 260.524 233.948 259.731 234.856C258.564 236.187 258.38 236.481 255.55 238.266C254.538 238.907 253.178 239.196 251.307 239.989C249.879 240.595 248.275 240.652 246.79 240.556C242.377 240.272 241.314 239.651 237.25 237.604C235.526 236.736 234.175 235.239 233.213 233.595C232.112 231.715 231.619 230.84 231.168 229.259C230.058 225.366 230.7 224.207 231.226 221.109C231.559 219.156 232.829 217.465 234.034 215.845C235.392 214.02 236.045 213.432 237.465 212.697C240.077 211.344 240.907 210.967 242.832 210.268Z"/>
              <path d="M183.457 113.776L183.174 113.364L183.174 113.364L183.457 113.776ZM209.297 102.564L209.193 102.075L209.193 102.075L209.297 102.564ZM147.45 143L147.785 143.37L147.786 143.37L147.45 143ZM127.971 174.197L128.438 174.375L128.438 174.375L127.971 174.197ZM127.789 174.676L128.256 174.854L128.256 174.854L127.789 174.676ZM117.997 220.821L117.5 220.876L117.5 220.876L117.997 220.821ZM119.152 233.161L119.65 233.119L119.65 233.119L119.152 233.161ZM135.64 284.872L136.068 284.613L136.068 284.613L135.64 284.872ZM161.033 315.012L160.68 315.366L160.68 315.366L161.033 315.012ZM201.07 338.817L201.184 338.33L201.184 338.33L201.07 338.817ZM205.411 339.83L205.297 340.317L205.297 340.317L205.411 339.83ZM281.216 343.903L281.129 343.41L281.129 343.41L281.216 343.903ZM314.798 330.896L315.104 331.292L315.104 331.292L314.798 330.896ZM328.754 320.989L329.033 321.404L329.033 321.404L328.754 320.989ZM343.704 309.334L343.337 308.995L343.336 308.996L343.704 309.334ZM367.434 276.65L366.982 276.435L366.982 276.435L367.434 276.65ZM368.382 274.66L368.833 274.875L368.833 274.874L368.382 274.66ZM368.617 274.166L368.166 273.951L368.166 273.951L368.617 274.166ZM380.632 243.958L381.121 244.064L381.121 244.063L380.632 243.958ZM374.509 185.827L374.033 185.98L374.033 185.98L374.509 185.827ZM362.616 159.801L363.014 159.498L363.014 159.498L362.616 159.801ZM361.689 158.583L361.291 158.886L361.291 158.886L361.689 158.583ZM323.377 119.183L323.071 119.578L323.071 119.578L323.377 119.183ZM288.473 101.102L288.347 101.586L288.347 101.586L288.473 101.102ZM285.646 100.352L285.516 100.835L285.516 100.835L285.646 100.352ZM246.723 97.0463L246.712 96.5464L246.712 96.5464L246.723 97.0463ZM241.049 96.9903L241.067 96.4907L241.049 96.9903ZM214.3 101.46L214.415 101.946L214.415 101.946L214.3 101.46ZM274.667 127.19L274.743 126.695L274.743 126.695L274.667 127.19ZM295.254 134.589L294.993 135.015L294.993 135.015L295.254 134.589ZM238.132 124.463L238.121 124.963L238.122 124.963L238.132 124.463ZM209.491 131.571L209.698 132.026L209.698 132.026L209.491 131.571ZM209.115 131.742L209.322 132.197L209.322 132.197L209.115 131.742ZM177.145 152.305L176.762 151.984L176.762 151.984L177.145 152.305ZM170.657 159.798L170.282 159.467L170.282 159.467L170.657 159.798ZM149.836 197.351L150.318 197.486L150.318 197.486L149.836 197.351ZM146.325 227.579L145.825 227.565L145.825 227.565L146.325 227.579ZM154.471 262.011L154.895 261.745L154.894 261.745L154.471 262.011ZM156.258 264.869L155.834 265.134L155.834 265.134L156.258 264.869ZM195.332 307.194L195.608 306.777L195.608 306.777L195.332 307.194ZM221.186 317.683L221.137 318.181L221.137 318.181L221.186 317.683ZM234.527 319.531L234.446 320.025L234.446 320.025L234.527 319.531ZM249.42 320.93L249.388 320.431L249.387 320.432L249.42 320.93ZM281.242 315.239L281.07 314.769L281.07 314.769L281.242 315.239ZM282.908 314.63L283.079 315.1L283.08 315.099L282.908 314.63ZM283.321 314.479L283.149 314.009L283.149 314.009L283.321 314.479ZM307.313 303.979L307.582 304.4L307.582 304.4L307.313 303.979ZM337.501 268.321L337.063 268.08L337.063 268.08L337.501 268.321ZM346.016 247.521L346.509 247.604L346.509 247.604L346.016 247.521ZM346.212 246.353L345.719 246.27L345.719 246.27L346.212 246.353ZM348.006 204.135L347.509 204.187L347.509 204.187L348.006 204.135ZM339.363 175.608L338.932 175.861L338.932 175.861L339.363 175.608ZM338.251 173.696L338.684 173.445L338.684 173.445L338.251 173.696ZM318.889 151.286L319.228 150.919L319.228 150.919L318.889 151.286ZM315.821 148.257L316.182 147.911L316.182 147.911L315.821 148.257ZM298.625 136.616L298.375 137.049L298.375 137.049L298.625 136.616ZM183.74 114.189C189.772 110.048 194.255 107.676 198.184 106.135C202.115 104.593 205.51 103.875 209.4 103.053L209.193 102.075C205.308 102.896 201.837 103.628 197.819 105.204C193.8 106.78 189.251 109.193 183.174 113.364L183.74 114.189ZM147.786 143.37C164.918 127.817 170.47 123.302 183.74 114.188L183.174 113.364C169.854 122.511 164.266 127.059 147.114 142.63L147.786 143.37ZM128.438 174.375C131.646 165.937 134.171 160.288 137.045 155.7C139.915 151.121 143.145 147.579 147.785 143.37L147.114 142.63C142.432 146.875 139.132 150.486 136.198 155.169C133.269 159.844 130.716 165.567 127.503 174.019L128.438 174.375ZM128.256 174.854L128.438 174.375L127.503 174.019L127.321 174.498L128.256 174.854ZM118.494 220.765C116.757 205.122 122.6 189.729 128.256 174.854L127.321 174.498C121.684 189.325 115.732 204.95 117.5 220.876L118.494 220.765ZM119.65 233.119C119.337 229.36 118.999 225.304 118.494 220.765L117.5 220.876C118.003 225.399 118.34 229.443 118.654 233.202L119.65 233.119ZM136.068 284.613C129.021 272.965 125.281 264.389 123.12 256.591C120.957 248.788 120.369 241.743 119.65 233.119L118.654 233.202C119.371 241.815 119.965 248.951 122.156 256.858C124.349 264.769 128.134 273.43 135.212 285.13L136.068 284.613ZM161.387 314.659C148.729 302.001 143.019 296.105 136.068 284.613L135.212 285.13C142.232 296.735 148.019 302.705 160.68 315.366L161.387 314.659ZM201.184 338.33C186.084 334.817 172.419 325.689 161.387 314.658L160.68 315.366C171.798 326.483 185.622 335.737 200.957 339.304L201.184 338.33ZM205.525 339.343C204.121 339.015 202.675 338.677 201.184 338.33L200.957 339.304C202.448 339.651 203.893 339.989 205.297 340.317L205.525 339.343ZM281.129 343.41C264.532 346.345 253.726 347.212 243.037 346.41C232.335 345.607 221.734 343.131 205.525 339.343L205.297 340.317C221.484 344.1 232.167 346.598 242.962 347.408C253.768 348.218 264.667 347.337 281.303 344.395L281.129 343.41ZM314.493 330.5C304.916 337.882 292.77 341.354 281.129 343.41L281.303 344.395C292.995 342.329 305.333 338.823 315.104 331.292L314.493 330.5ZM328.474 320.575C324.313 323.382 319.635 326.537 314.493 330.5L315.104 331.292C320.217 327.35 324.871 324.211 329.033 321.404L328.474 320.575ZM343.336 308.996C339.584 313.078 334.609 316.437 328.474 320.575L329.033 321.404C335.14 317.285 340.224 313.859 344.073 309.673L343.336 308.996ZM366.982 276.435C364.365 281.939 362.672 285.498 359.532 289.966C356.386 294.444 351.782 299.843 343.337 308.995L344.072 309.673C352.518 300.52 357.163 295.078 360.35 290.541C363.544 285.995 365.27 282.365 367.886 276.864L366.982 276.435ZM367.931 274.444C367.6 275.136 367.285 275.799 366.982 276.435L367.886 276.864C368.188 276.228 368.503 275.566 368.833 274.875L367.931 274.444ZM368.166 273.951L367.931 274.445L368.833 274.874L369.068 274.381L368.166 273.951ZM380.144 243.853C378.201 252.859 372.275 265.317 368.166 273.951L369.068 274.381C373.158 265.787 379.148 253.209 381.121 244.064L380.144 243.853ZM374.033 185.98C380.606 206.389 384.469 223.766 380.144 243.853L381.121 244.063C385.504 223.711 381.572 206.126 374.985 185.673L374.033 185.98ZM362.218 160.103C368.131 167.875 371.168 177.079 374.033 185.98L374.985 185.674C372.126 176.793 369.046 167.426 363.014 159.498L362.218 160.103ZM361.291 158.886C361.595 159.285 361.904 159.691 362.218 160.103L363.014 159.498C362.7 159.085 362.391 158.679 362.087 158.28L361.291 158.886ZM323.071 119.578C333.177 127.386 339.013 132.331 344.177 137.757C349.345 143.186 353.85 149.106 361.291 158.886L362.087 158.28C354.656 148.514 350.116 142.545 344.901 137.067C339.683 131.585 333.798 126.603 323.683 118.787L323.071 119.578ZM288.347 101.586C302.386 105.259 311.581 110.698 323.071 119.578L323.683 118.787C312.125 109.854 302.809 104.336 288.6 100.619L288.347 101.586ZM285.516 100.835C286.41 101.074 287.347 101.324 288.347 101.586L288.6 100.619C287.604 100.358 286.669 100.108 285.775 99.8688L285.516 100.835ZM246.735 97.5461C258.947 97.2624 266.199 97.4339 271.617 98.0001C277.024 98.5652 280.613 99.5241 285.516 100.835L285.775 99.8688C280.869 98.5572 277.213 97.5795 271.721 97.0055C266.238 96.4325 258.933 96.2625 246.712 96.5464L246.735 97.5461ZM241.031 97.49C242.49 97.5429 244.206 97.6052 246.735 97.5461L246.712 96.5464C244.213 96.6047 242.521 96.5434 241.067 96.4907L241.031 97.49ZM214.415 101.946C224.325 99.5855 229.788 98.4291 233.372 97.8834C236.936 97.341 238.634 97.4031 241.031 97.49L241.067 96.4907C238.641 96.4027 236.873 96.3391 233.222 96.8948C229.591 97.4475 224.091 98.6132 214.184 100.973L214.415 101.946ZM209.4 103.053C210.971 102.722 212.622 102.373 214.415 101.946L214.184 100.973C212.405 101.396 210.765 101.743 209.193 102.075L209.4 103.053ZM274.59 127.684C280.27 128.561 284.079 129.605 287.105 130.817C290.132 132.03 292.393 133.418 294.993 135.015L295.516 134.163C292.919 132.568 290.592 131.137 287.477 129.889C284.361 128.64 280.474 127.581 274.743 126.695L274.59 127.684ZM238.122 124.963C256.454 125.341 262.088 125.756 274.59 127.684L274.743 126.695C262.181 124.758 256.5 124.342 238.142 123.964L238.122 124.963ZM209.698 132.026C216.318 129.015 220.951 127.202 225.162 126.163C229.363 125.127 233.163 124.859 238.121 124.963L238.142 123.964C233.13 123.858 229.236 124.129 224.922 125.192C220.618 126.254 215.916 128.099 209.284 131.116L209.698 132.026ZM209.322 132.197L209.698 132.026L209.284 131.116L208.908 131.287L209.322 132.197ZM177.528 152.626C185.591 142.999 197.647 137.507 209.322 132.197L208.908 131.287C197.278 136.576 184.996 142.152 176.762 151.984L177.528 152.626ZM171.032 160.129C173.029 157.867 175.185 155.425 177.528 152.626L176.762 151.984C174.428 154.772 172.28 157.205 170.282 159.467L171.032 160.129ZM150.318 197.486C153.185 187.274 156.085 180.523 159.397 175.041C162.712 169.554 166.449 165.32 171.032 160.129L170.282 159.467C165.707 164.649 161.91 168.948 158.541 174.524C155.17 180.104 152.239 186.943 149.355 197.216L150.318 197.486ZM146.825 227.593C147.21 213.847 147.491 207.554 150.318 197.486L149.355 197.216C146.492 207.413 146.21 213.813 145.825 227.565L146.825 227.593ZM154.894 261.745C148.69 251.84 146.49 239.559 146.825 227.593L145.825 227.565C145.487 239.656 147.705 252.151 154.047 262.276L154.894 261.745ZM156.682 264.604C156.104 263.679 155.509 262.727 154.895 261.745L154.047 262.276C154.661 263.257 155.256 264.209 155.834 265.134L156.682 264.604ZM195.608 306.777C184.85 299.647 178.456 294.429 173.089 288.347C167.714 282.256 163.356 275.284 156.682 264.604L155.834 265.134C162.495 275.793 166.899 282.843 172.339 289.009C177.788 295.184 184.264 300.458 195.056 307.611L195.608 306.777ZM221.235 317.186C211.769 316.245 203.148 311.776 195.608 306.777L195.056 307.611C202.644 312.641 211.428 317.216 221.137 318.181L221.235 317.186ZM234.607 319.038C230.714 318.405 226.335 317.692 221.235 317.186L221.137 318.181C226.201 318.684 230.553 319.392 234.446 320.025L234.607 319.038ZM249.387 320.432C244.993 320.725 240.349 319.972 234.607 319.038L234.446 320.025C240.157 320.954 244.923 321.732 249.453 321.429L249.387 320.432ZM281.07 314.769C276.464 316.456 273.491 317.545 269.204 318.377C264.908 319.211 259.282 319.789 249.388 320.431L249.452 321.429C259.349 320.787 265.03 320.206 269.395 319.358C273.769 318.509 276.812 317.394 281.414 315.708L281.07 314.769ZM282.737 314.16C282.157 314.371 281.602 314.574 281.07 314.769L281.414 315.708C281.946 315.513 282.5 315.311 283.079 315.1L282.737 314.16ZM283.149 314.009L282.736 314.16L283.08 315.099L283.493 314.948L283.149 314.009ZM307.044 303.558C300.795 307.549 290.378 311.364 283.149 314.009L283.493 314.948C290.682 312.317 301.22 308.464 307.582 304.4L307.044 303.558ZM337.063 268.08C328.884 282.931 320.979 294.65 307.044 303.558L307.582 304.4C321.733 295.355 329.738 283.455 337.939 268.562L337.063 268.08ZM345.523 247.439C344.275 254.876 340.634 261.599 337.063 268.08L337.939 268.562C341.499 262.102 345.228 255.235 346.509 247.604L345.523 247.439ZM345.719 246.27C345.655 246.653 345.59 247.043 345.523 247.439L346.509 247.604C346.576 247.208 346.641 246.819 346.705 246.435L345.719 246.27ZM347.509 204.187C348.527 213.879 348.862 219.712 348.555 225.456C348.247 231.207 347.295 236.881 345.719 246.27L346.705 246.435C348.279 237.064 349.242 231.329 349.553 225.51C349.865 219.684 349.522 213.788 348.503 204.082L347.509 204.187ZM338.932 175.861C344.471 185.304 346.354 193.174 347.509 204.187L348.503 204.082C347.34 192.981 345.428 184.96 339.794 175.355L338.932 175.861ZM337.818 173.946C338.169 174.551 338.537 175.187 338.932 175.861L339.794 175.355C339.401 174.684 339.034 174.051 338.684 173.445L337.818 173.946ZM318.55 151.654C325.386 157.948 329.244 161.87 331.872 165.04C334.492 168.203 335.895 170.625 337.818 173.946L338.684 173.445C336.759 170.121 335.321 167.635 332.642 164.402C329.97 161.178 326.071 157.219 319.228 150.919L318.55 151.654ZM315.46 148.603C316.227 149.404 317.131 150.348 318.55 151.654L319.228 150.919C317.832 149.634 316.945 148.708 316.182 147.911L315.46 148.603ZM298.375 137.049C305.152 140.968 308.8 143.207 311.068 144.793C313.318 146.367 314.203 147.292 315.46 148.603L316.182 147.911C314.904 146.577 313.967 145.6 311.641 143.974C309.333 142.36 305.651 140.102 298.876 136.183L298.375 137.049ZM294.993 135.015C296.042 135.66 297.147 136.339 298.375 137.049L298.876 136.184C297.661 135.481 296.567 134.808 295.516 134.163L294.993 135.015Z" fill="white"/>
            </svg>
          </div>
        </div>
      )
  }

  function handlePreviousSlideChange() {
    setCurrentSlide(prevData => {
      const oldNum = prevData
      let newNum
      // Preventing going under zero
      if (oldNum > 0) {
        newNum = oldNum - 1
      } else  {
        newNum = 0
      }
      return newNum
    })
  }
  function handleNextSlideChange() {
    setCurrentSlide(prevData => {
      const oldNum = prevData
      const maxNum = allSlides.length - 1
      let newNum
      // Preventing going over top
      if (oldNum < maxNum) {
        newNum = oldNum + 1
      } else  {
        newNum = maxNum
      }
      return newNum
    })
  }
}

