from transformers import pipeline

def wordCount(article):
    return(len(article.strip().split(" ")))

def summariser(result):
    
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        #out = summarizer(result[start:end], min_length = int(0.1*len(result)), max_length = int(0.2*len(result)))
        out = summarizer(result[start:end], min_length=30, max_length=50)
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)

    # print("Original Word Length: ", wordCount(result))
    # print("Summarized Word Length: ", wordCount(summarized_text))
    return summarized_text

#result = "Mohandas Karamchand Gandhi was an Indian lawyer, anti-colonial nationalist and political ethicist who employed nonviolent resistance to lead the successful campaign for India's independence from British rule and in turn inspired movements for civil rights and freedom across the world. The honorific Mahātmā, first applied to him in 1914 in South Africa, is now used throughout the world.\n Born and raised in a Hindu family in coastal Gujarat, Gandhi trained in law at the Inner Temple, London, and was called to the bar at age 22 in June 1891. After two uncertain years in India, where he was unable to start a successful law practice, he moved to South Africa in 1893 to represent an Indian merchant in a lawsuit. He went on to live in South Africa for 21 years. It was in South Africa that Gandhi raised a family and first employed nonviolent resistance in a campaign for civil rights. In 1915, aged 45, he returned to India. He set about organising peasants, farmers, and urban labourers to protest against excessive land-tax and discrimination. Assuming leadership of the Indian National Congress in 1921, Gandhi led nationwide campaigns for easing poverty, expanding women's rights, building religious and ethnic amity, ending untouchability, and above all for achieving swaraj or self-rule. \n Also in 1921, Gandhi adopted the use of an Indian loincloth (short dhoti) and a shawl (in the winter) woven with yarn hand-spun on a traditional Indian spinning wheel (charkha) as a sign of identification with India's rural poor. He also began to live modestly in a self-sufficient residential community, ate simple vegetarian food, and undertook long fasts as a means of self-purification and political protest. Bringing anti-colonial nationalism to the common Indians, Gandhi led them in challenging the British-imposed salt tax with the 400 km (250 mi) Dandi Salt March in 1930 and in calling for the British to quit India in 1942. He was imprisoned many times and for many years in both South Africa and India. \n Gandhi's vision of an independent India based on religious pluralism was challenged in the early 1940s by a new Muslim nationalism which demanded a separate Muslim homeland carved out of India. In August 1947, Britain granted independence, but the British Indian Empirewas partitioned into two dominions, the Hindu-majority India and the Muslim-majority Pakistan. Nathuram Godse, a Hindu nationalist assassinated Gandhi on 30 January 1948 by firing three bullets into his chest."
#print(summariser(result))