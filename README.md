# Summarization

[![Awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=Awesome+plugin&color=000000&style=for-the-badge&logo=cheshire_cat_ai)](https://)  

This plugin hooks into the `RabbitHole` to ask the Language Model to summarize groups of text chunks. 
Summaries are stored in the vector memory, along with the original chunks.  

The summarization can help the Cat to have a more comprehensive understanding of the content of the documents.

> **Warning**
> The summarization increases considerably the uploading time if the document size is big.  
> Moreover, when this plugin is enabled the Cat makes and additional call to the language model API.