from uuid import UUID, getnode, uuid4


def get_agent_id() -> UUID:
    """
    Get the agent ID for the current running agent

    Each time an agent process starts, the return value of this function will be unique. Subsequent
    calls to this function from within the same process will have the same return value.
    """
    if get_agent_id._id is None:
        get_agent_id._id = uuid4()

    return get_agent_id._id


get_agent_id._id = None


def get_machine_id() -> int:
    """Get an integer that uniquely defines the machine the agent is running on"""
    return getnode()
