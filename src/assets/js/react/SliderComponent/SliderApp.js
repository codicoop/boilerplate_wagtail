import React, { useEffect, useState } from 'react';
import { useTranslation } from "react-i18next"
import axios from 'axios';
import './i18n';

export default function SliderApp(){
  const [currentSlide, setCurrentSlide] = useState("0")
  const { t, i18n } = useTranslation()

  return (
    <>
      <div className="slider grid-2">
        <div className="slider__controller grid-item-4-9">
          <div className="slider__btn" data-value="0" onClick={handleSlideChange}>
            {
              currentSlide === "0"
              ? <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="16" cy="16" r="16" fill="#303030" stroke="#303030" strokeWidth="2"/>
                  <path d="M22.0721 21.409C20.7204 22.793 18.85 23.6534 16.7896 23.6534C12.6615 23.6459 9.31515 20.2195 9.31515 16C9.31515 11.7731 12.6615 8.34663 16.7896 8.34663C18.85 8.34663 20.7204 9.1995 22.0721 10.591L23 9.6409C21.4072 8.00997 19.2153 7 16.7896 7C11.9308 7 8 11.0249 8 16C8 20.9676 11.9308 25 16.7896 25C19.2153 25 21.4145 23.99 23 22.3666L22.0721 21.409Z" fill="white"/>
                  <path d="M11 16C11 19.3135 13.6235 22 16.8594 22C18.4739 22 19.9422 21.3302 21 20.2399L20.1093 19.3278C19.2742 20.1829 18.126 20.7102 16.8525 20.7102C14.3125 20.7102 12.2526 18.601 12.2526 16C12.2526 13.3991 14.3125 11.2898 16.8525 11.2898C18.126 11.2898 19.2742 11.8171 20.1093 12.6722L21 11.7601C19.9422 10.677 18.4739 10 16.8594 10C13.6235 10 11 12.6865 11 16Z" fill="white"/>
                </svg>
              : <p>0</p>
            }
          </div>
          <div className="slider__btn" data-value="1" onClick={handleSlideChange}>
            {
              currentSlide === "1"
              ? <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="16" cy="16" r="16" fill="#303030" stroke="#303030" strokeWidth="2"/>
                  <path d="M22.0721 21.409C20.7204 22.793 18.85 23.6534 16.7896 23.6534C12.6615 23.6459 9.31515 20.2195 9.31515 16C9.31515 11.7731 12.6615 8.34663 16.7896 8.34663C18.85 8.34663 20.7204 9.1995 22.0721 10.591L23 9.6409C21.4072 8.00997 19.2153 7 16.7896 7C11.9308 7 8 11.0249 8 16C8 20.9676 11.9308 25 16.7896 25C19.2153 25 21.4145 23.99 23 22.3666L22.0721 21.409Z" fill="white"/>
                  <path d="M11 16C11 19.3135 13.6235 22 16.8594 22C18.4739 22 19.9422 21.3302 21 20.2399L20.1093 19.3278C19.2742 20.1829 18.126 20.7102 16.8525 20.7102C14.3125 20.7102 12.2526 18.601 12.2526 16C12.2526 13.3991 14.3125 11.2898 16.8525 11.2898C18.126 11.2898 19.2742 11.8171 20.1093 12.6722L21 11.7601C19.9422 10.677 18.4739 10 16.8594 10C13.6235 10 11 12.6865 11 16Z" fill="white"/>
                </svg>
              : <p>1</p>
            }
          </div>
          <div className="slider__btn" data-value="2" onClick={handleSlideChange}>
            {
              currentSlide === "2"
              ? <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="16" cy="16" r="16" fill="#303030" stroke="#303030" strokeWidth="2"/>
                  <path d="M22.0721 21.409C20.7204 22.793 18.85 23.6534 16.7896 23.6534C12.6615 23.6459 9.31515 20.2195 9.31515 16C9.31515 11.7731 12.6615 8.34663 16.7896 8.34663C18.85 8.34663 20.7204 9.1995 22.0721 10.591L23 9.6409C21.4072 8.00997 19.2153 7 16.7896 7C11.9308 7 8 11.0249 8 16C8 20.9676 11.9308 25 16.7896 25C19.2153 25 21.4145 23.99 23 22.3666L22.0721 21.409Z" fill="white"/>
                  <path d="M11 16C11 19.3135 13.6235 22 16.8594 22C18.4739 22 19.9422 21.3302 21 20.2399L20.1093 19.3278C19.2742 20.1829 18.126 20.7102 16.8525 20.7102C14.3125 20.7102 12.2526 18.601 12.2526 16C12.2526 13.3991 14.3125 11.2898 16.8525 11.2898C18.126 11.2898 19.2742 11.8171 20.1093 12.6722L21 11.7601C19.9422 10.677 18.4739 10 16.8594 10C13.6235 10 11 12.6865 11 16Z" fill="white"/>
                </svg>
              : <p>2</p>
            }
          </div>
          <div className="slider__btn" data-value="3" onClick={handleSlideChange}>
          {
              currentSlide === "3"
              ? <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="16" cy="16" r="16" fill="#303030" stroke="#303030" strokeWidth="2"/>
                  <path d="M22.0721 21.409C20.7204 22.793 18.85 23.6534 16.7896 23.6534C12.6615 23.6459 9.31515 20.2195 9.31515 16C9.31515 11.7731 12.6615 8.34663 16.7896 8.34663C18.85 8.34663 20.7204 9.1995 22.0721 10.591L23 9.6409C21.4072 8.00997 19.2153 7 16.7896 7C11.9308 7 8 11.0249 8 16C8 20.9676 11.9308 25 16.7896 25C19.2153 25 21.4145 23.99 23 22.3666L22.0721 21.409Z" fill="white"/>
                  <path d="M11 16C11 19.3135 13.6235 22 16.8594 22C18.4739 22 19.9422 21.3302 21 20.2399L20.1093 19.3278C19.2742 20.1829 18.126 20.7102 16.8525 20.7102C14.3125 20.7102 12.2526 18.601 12.2526 16C12.2526 13.3991 14.3125 11.2898 16.8525 11.2898C18.126 11.2898 19.2742 11.8171 20.1093 12.6722L21 11.7601C19.9422 10.677 18.4739 10 16.8594 10C13.6235 10 11 12.6865 11 16Z" fill="white"/>
                </svg>
              : <p>3</p>
            }
          </div>
          <div className="slider__btn" data-value="4" onClick={handleSlideChange}>
          {
              currentSlide === "4"
              ? <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="16" cy="16" r="16" fill="#303030" stroke="#303030" strokeWidth="2"/>
                  <path d="M22.0721 21.409C20.7204 22.793 18.85 23.6534 16.7896 23.6534C12.6615 23.6459 9.31515 20.2195 9.31515 16C9.31515 11.7731 12.6615 8.34663 16.7896 8.34663C18.85 8.34663 20.7204 9.1995 22.0721 10.591L23 9.6409C21.4072 8.00997 19.2153 7 16.7896 7C11.9308 7 8 11.0249 8 16C8 20.9676 11.9308 25 16.7896 25C19.2153 25 21.4145 23.99 23 22.3666L22.0721 21.409Z" fill="white"/>
                  <path d="M11 16C11 19.3135 13.6235 22 16.8594 22C18.4739 22 19.9422 21.3302 21 20.2399L20.1093 19.3278C19.2742 20.1829 18.126 20.7102 16.8525 20.7102C14.3125 20.7102 12.2526 18.601 12.2526 16C12.2526 13.3991 14.3125 11.2898 16.8525 11.2898C18.126 11.2898 19.2742 11.8171 20.1093 12.6722L21 11.7601C19.9422 10.677 18.4739 10 16.8594 10C13.6235 10 11 12.6865 11 16Z" fill="white"/>
                </svg>
              : <p>4</p>
            }
          </div>
          <div className="slider__btn" data-value="5" onClick={handleSlideChange}>
            {
              currentSlide === "5"
              ? <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="16" cy="16" r="16" fill="#303030" stroke="#303030" strokeWidth="2"/>
                  <path d="M22.0721 21.409C20.7204 22.793 18.85 23.6534 16.7896 23.6534C12.6615 23.6459 9.31515 20.2195 9.31515 16C9.31515 11.7731 12.6615 8.34663 16.7896 8.34663C18.85 8.34663 20.7204 9.1995 22.0721 10.591L23 9.6409C21.4072 8.00997 19.2153 7 16.7896 7C11.9308 7 8 11.0249 8 16C8 20.9676 11.9308 25 16.7896 25C19.2153 25 21.4145 23.99 23 22.3666L22.0721 21.409Z" fill="white"/>
                  <path d="M11 16C11 19.3135 13.6235 22 16.8594 22C18.4739 22 19.9422 21.3302 21 20.2399L20.1093 19.3278C19.2742 20.1829 18.126 20.7102 16.8525 20.7102C14.3125 20.7102 12.2526 18.601 12.2526 16C12.2526 13.3991 14.3125 11.2898 16.8525 11.2898C18.126 11.2898 19.2742 11.8171 20.1093 12.6722L21 11.7601C19.9422 10.677 18.4739 10 16.8594 10C13.6235 10 11 12.6865 11 16Z" fill="white"/>
                </svg>
              : <p>5</p>
            }
          </div>
        </div>
        <div className="slider__info grid-item-1-6">
          <div className="slider__title title-1--light">
            <p>{t('How_we_do_it')}</p>
          </div>
          <div className="slider__text">
            {
              currentSlide === "0" &&
              <p>TEXT BLOCK 0 Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet luctus venenatis, lectus magna fringilla urna, porttitor rhoncus dolor Purus non enim praesent elementum facilisis leo, vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet.</p> 
            }
            {
              currentSlide === "1" &&
              <p>TEXT BLOCK 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet luctus venenatis, lectus magna fringilla urna, porttitor rhoncus dolor Purus non enim praesent elementum facilisis leo, vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet.</p> 
            }
            {
              currentSlide === "2" &&
              <p>TEXT BLOCK 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet luctus venenatis, lectus magna fringilla urna, porttitor rhoncus dolor Purus non enim praesent elementum facilisis leo, vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet.</p> 
            }
            {
              currentSlide === "3" &&
              <p>TEXT BLOCK 3 Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet luctus venenatis, lectus magna fringilla urna, porttitor rhoncus dolor Purus non enim praesent elementum facilisis leo, vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet.</p> 
            }
            {
              currentSlide === "4" &&
              <p>TEXT BLOCK 4 Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet luctus venenatis, lectus magna fringilla urna, porttitor rhoncus dolor Purus non enim praesent elementum facilisis leo, vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet.</p> 
            }
            {
              currentSlide === "5" &&
              <p>TEXT BLOCK 5 Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam, purus sit amet luctus venenatis, lectus magna fringilla urna, porttitor rhoncus dolor Purus non enim praesent elementum facilisis leo, vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet.</p> 
            }
          </div>
        </div>
        <div className="slider__video grid-item-7-12">
          {
            currentSlide === "0" &&
            <iframe 
              className='slider__iframe'
              src="https://www.youtube-nocookie.com/embed/x_jQiV26uQc" 
              title="YouTube video player" 
              frameBorder="0" 
              allow="web-share" 
              allowFullScreen></iframe>
          }
          {
            currentSlide === "1" &&
            <iframe 
              className='slider__iframe'
              src="https://www.youtube-nocookie.com/embed/SZrLUayVYUk" 
              title="YouTube video player" 
              frameBorder="0" 
              allow="web-share" 
              allowFullScreen></iframe>
          }
          {
            currentSlide === "2" &&
            <iframe 
              className='slider__iframe'
              src="https://www.youtube-nocookie.com/embed/rdojQLWP2HU" 
              title="YouTube video player" 
              frameBorder="0" 
              allow="web-share" 
              allowFullScreen></iframe>
          }
          {
            currentSlide === "3" &&
            <iframe 
              className='slider__iframe'
              src="https://www.youtube-nocookie.com/embed/b3gyDh5tFNI" 
              title="YouTube video player" 
              frameBorder="0" 
              allow="web-share" 
              allowFullScreen></iframe>
          }
          {
            currentSlide === "4" &&
            <iframe 
              className='slider__iframe'
              src="https://www.youtube-nocookie.com/embed/rWTLrpWXNJc" 
              title="YouTube video player" 
              frameBorder="0" 
              allow="web-share" 
              allowFullScreen></iframe>
          }
          {
            currentSlide === "5" &&
            <iframe 
              className='slider__iframe'
              src="https://www.youtube-nocookie.com/embed/-HyxleazCKs" 
              title="YouTube video player" 
              frameBorder="0" 
              allow="web-share" 
              allowFullScreen></iframe>
          }
        </div>
      </div>
    </>
  )

  function handleSlideChange(event) {
    const value = event.target.dataset.value
    setCurrentSlide(value)
  }
}

