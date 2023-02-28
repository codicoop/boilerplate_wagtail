import i18n from "i18next";
import { initReactI18next } from "react-i18next";


// Importing translation files
import translationES from "./locales/es/translation.json";
import translationCA from "./locales/ca/translation.json";


// Creating object with the variables of imported translation files
const resources = {
  es: {
    translation: translationES,
  },
  ca: {
    translation: translationCA,
  },
};

// i18N Initialization

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng:"ca", // default language
    keySeparator: false,
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;