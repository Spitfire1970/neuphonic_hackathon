import os
import asyncio

from pyneuphonic import Neuphonic, Agent, AgentConfig

api_key = "fd670d8dde423652a2b03922b9c3178a781191c6e5c51a3a5501ffbba752d2db.b572ca47-5ec5-461b-82a0-e28fefeed32f" # GET THIS FROM beta.neuphonic.com!!!!!!!!!

async def main():
    client = Neuphonic(api_key=api_key)

    agent_id = client.agents.create(
        name='Agent 1',
        prompt='im gonna tell you a story and then ask you to complete it',
        greeting='Hi, how can I help you today?'
    )['data']['id']

    agent = Agent(client, agent_id=agent_id, tts_model='neu_hq')

    await agent.start()

asyncio.run(main())
