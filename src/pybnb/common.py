"""
Basic definitions and utilities.

Copyright by Gabriel A. Hackebeil (gabe.hackebeil@gmail.com).
"""

import enum

minimize = 1
"""The objective sense defining a minimization problem."""

maximize = -1
"""The objective sense defining a maximization problem."""

inf = float("inf")
"""A floating point constant set to ``float('inf')``."""

nan = float("nan")
"""A floating point constant set to ``float('nan')``."""

@enum.unique
class NodePriorityStrategy(str, enum.Enum):
    """Strategies for prioritizing nodes in the central
    dispatcher queue. For all strategies, ties are broken by
    insertion order."""
    _order_ = ("bound "
               "objective "
               "breadth "
               "depth "
               "fifo "
               "random "
               "custom")

    bound = "bound"
    """The node with the worst bound is always selected
    next."""
    objective = "objective"
    """The node with the best objective is always selected
    next."""
    breadth = "breadth"
    """The node with the smallest tree depth is always
    selected next (i.e., breadth-first search)."""
    depth = "depth"
    """The node with the largest tree depth is always
    selected next (i.e., depth-first search)."""
    fifo = "fifo"
    """Nodes are served in first-in, first-out order."""
    random = "random"
    """Nodes are assigned a random priorities before
    entering the queue."""
    custom = "custom"
    """The node with the largest value stored in the
    :attr:`queue_priority <pybnb.node.Node.queue_priority>`
    attribute is always selected next. Users are expected to
    assign a priority to all nodes returned from the
    :func:`branch <pybnb.problem.Problem.branch>`
    method on their problem."""
_node_priority_strategy_to_int = {}
_int_to_node_priority_strategy = []
for _i, _val in enumerate(NodePriorityStrategy):
    _node_priority_strategy_to_int[_val] = _i
    _int_to_node_priority_strategy.append(_val)
del _i
del _val

@enum.unique
class SolutionStatus(str, enum.Enum):
    """Possible values assigned to the
    :attr:`solution_status` attribute of a
    :class:`SolverResults <pybnb.solver.SolverResults>`
    object returned from a solve."""
    _order_ = ("optimal "
               "feasible "
               "infeasible "
               "unbounded "
               "invalid "
               "unknown")

    optimal = "optimal"
    """Indicates that the best objective is finite and close
    enough to the global bound to satisfy the optimality
    tolerances used for the solve."""
    feasible = "feasible"
    """Indicates that the best objective is finite but not
    close enough to the global bound to satisfy the
    optimality tolerances used for the solve."""
    infeasible = "infeasible"
    """Indicates that both the best objective and global
    bound are equal to the infeasible objective value (+inf
    or -inf depending on the sense)."""
    unbounded = "unbounded"
    """Indicates that both the best objective and global
    bound are equal to the unbounded objective value (+inf
    or -inf depending on the sense)."""
    invalid = "invalid"
    """Indicates that the global bound is not a valid bound
    on the best objective found. This may be due to an
    ill-defined problem or other numerical issues."""
    unknown = "unknown"
    """Indicates that the global bound is finite, but no
    feasible (finite) objective was found."""
_solution_status_to_int = {}
_int_to_solution_status = []
for _i, _val in enumerate(SolutionStatus):
    _solution_status_to_int[_val] = _i
    _int_to_solution_status.append(_val)
del _i
del _val

@enum.unique
class TerminationCondition(str, enum.Enum):
    """Possible values assigned to the
    :attr:`termination_condition` attribute of a
    :class:`SolverResults <pybnb.solver.SolverResults>`
    object returned from a solve."""
    _order_ = ("optimality "
               "cutoff "
               "node_limit "
               "time_limit "
               "no_nodes "
               "interrupted")

    optimality = "optimality"
    """The dispatcher terminated the solve based on
    optimality criteria."""
    cutoff = "cutoff"
    """The dispatcher terminated the solve based on the
    user-supplied objective cutoff being satisfied."""
    node_limit = "node_limit"
    """The dispatcher terminated the solve due to the
    user-supplied explored node limit being surpassed."""
    time_limit = "time_limit"
    """The dispatcher terminated the solve due to the
    user-supplied time limit being surpassed."""
    no_nodes = "no_nodes"
    """The dispatcher terminated the solve due to the node
    queue becoming empty."""
    interrupted = "interrupted"
    """Solve termination was initiated by SIGINT or SIGUSR
    signal event."""
_termination_condition_to_int = {}
_int_to_termination_condition = []
for _i, _val in enumerate(TerminationCondition):
    _termination_condition_to_int[_val] = _i
    _int_to_termination_condition.append(_val)
del _i
del _val
