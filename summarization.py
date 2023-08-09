import langchain
from langchain.docstore.document import Document
from cat.mad_hatter.decorators import hook
from cat.log import log


@hook
def before_rabbithole_stores_documents(docs, cat):
    summarization_prompt = """Write a concise summary of the following:
    {text}
    """  # TODO make this a setting
    summarization_chain = langchain.chains.LLMChain(
        llm=cat.llm,
        verbose=False,
        prompt=langchain.PromptTemplate(template=summarization_prompt,
                                        input_variables=["text"]),
    )

    # we will store iterative summaries all together in a list
    all_summaries = []

    summarization_level = 0  # 0 means hierarchical?  # TODO make this a setting
    group_size = 5  # TODO make this a setting
    separator = "\n --> "

    # make summaries of groups of docs
    for i in range(0, len(docs), group_size):
        group = docs[i: i + group_size]
        group = list(map(lambda d: d.page_content, group))

        text_to_summarize = separator + separator.join(group)
        summary = summarization_chain.run(text_to_summarize)
        summary = Document(page_content=summary)
        summary.metadata["is_summary"] = True

        # add summary to list of all summaries
        all_summaries.append(summary)

    return all_summaries
