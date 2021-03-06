from abc import ABC, abstractmethod


class Layer(ABC):
    """Base class for all layers implementations."""

    @abstractmethod
    def forward(self, *args):
        """Should perform a local forward pass of the layer. Parameters
        should be the inputs to the layer and the outputs of the layer
        should be returned."""
        pass

    @abstractmethod
    def backward(self, *args):
        """Should perform a local backward pass of the layer. Parameters
        should be the gradients from the top (i.e. how layer's outputs
        influence the loss) and the gradients on inputs to the layer should
        be returned."""
        pass

    @property
    def has_updatable_params(self):
        """Indicates whether the layer has parameters that should be
        backproped into or not."""
        try:
            self.updatable_params_grads_names()
        except NotImplementedError:
            return False

        return True

    def updatable_params_grads_names(self):
        """Should expose all parameters and gradients name pairs (object's
        named attributes) that are backproped into. Should return a list
        of nnlib.optimizers.ParamGradNames namedtuples.
        """
        raise NotImplementedError()
