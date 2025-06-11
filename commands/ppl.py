import discord
import requests
import json


## getting people names from tv api
def __get_people_print_multiple(who):
    response = requests.get(f'https://api.tvmaze.com/search/people{who}')
    json_data = json.loads(response.text)

    if not json_data:
        return 'no names found in database matching what was inputted into the chat'

    results_data = []
    for item_dict in json_data[:5]:
        person_data = item_dict.get('person')

        if person_data:
           name = person_data.get('name')
           image_data = person_data.get('image')

           if image_data:
             medium_image_url = image_data.get('medium')

        if name:
           results_data.append({
              'name': name,
              'image' : medium_image_url,
           })

    if results_data:
      # You'll likely want to return the list of dictionaries, not a joined string
      return results_data
    else:
      return 'no suitable items found in the first 5 results'


async def command_ppl(message):
    search_text = '?q=' + message.content[len('`ppl'):].strip()

    people_results = __get_people_print_multiple(search_text)

    if not people_results:
      await message.channel.send('Sorry, I couldn\'t find anyone with that name in the tvmaze api database')
      await message.channel.send('Please check the logs in case I ran into an error fetching this data for you!')

    response_message = '## Top 5 People Matches: \n'

    for i, person in enumerate(people_results):
      name = person.get('name', 'N/A')
      image_url = person.get('image')

      response_message += f'{i+1}. **{name}**'

      if image_url:
        response_message += f' : [Image]({image_url})\n'

      if len(response_message) > 2000:
        response_message = response_message[:1990] + "...\n(Message too long, truncated)"

    await message.channel.send('Based on your search, here are the top matches from the TVMaze API database')
    await message.channel.send(response_message)
