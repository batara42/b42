module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("*.css");
  eleventyConfig.addPassthroughCopy("*.js");
  eleventyConfig.addPassthroughCopy("*.jpg");

  return {
    dir: {
      input: ".",
      output: "_site",
      data: "_data"
    },
    templateFormats: ["liquid", "html"],
    htmlTemplateEngine: "liquid"
  };
};
