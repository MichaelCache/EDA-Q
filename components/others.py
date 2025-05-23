from base.cmpnts_base import CmpntsBase
from addict import Dict
import func_modules
import copy

class Others(CmpntsBase):
    """
    Others class, inherited from CmpntsBase, used for managing and operating components of other types.
    """

    def __init__(self, **init_ops):
        """
        Initialize the Others object.

        Input:
            init_ops: dict, parameters required for initialization.

        Output:
            None
        """
        self.initialization(**init_ops)  # Call initialization method
        return
    
    def initialization(self, **init_ops):
        """
        Initialize the collection of other components.

        Input:
            init_ops: dict, parameters for generating the collection of other components.

        Output:
            None
        """
        # Initialize component name list
        self.cmpnt_name_list = []
        # Call the function module to generate options for other components
        options = func_modules.others.generate_others(**init_ops)
        self.inject_options(options)  # Inject generated parameters
        return
    
    def mirror_ZlineNju(self, name_list):
        """
        Perform horizontal mirroring operation on the specified ZlineNju components.

        Input:
            name_list: list, contains the names of components that need to be mirrored.

        Output:
            None
        """
        # Get the current parameter set of ZlineNju components
        zline_njus_ops = self.options
        for name in name_list:
            # Extract the original component parameters
            zline_nju_ops = copy.deepcopy(zline_njus_ops[name])
            
            # Create a parameter copy of the mirrored component
            new_zline_nju_ops = copy.deepcopy(zline_nju_ops)
            new_name = name + "_mirror"  # Mirrored component name
            new_zline_nju_ops.name = new_name

            # Mirror the initial position horizontally
            line_init_pos = copy.deepcopy(zline_nju_ops.line_init_pos)
            new_line_init_pos = []
            for pos in line_init_pos:
                new_pos = (-pos[0], pos[1])  # Horizontal mirror operation (negate x-coordinate)
                new_line_init_pos.append(copy.deepcopy(new_pos))
            new_zline_nju_ops.line_init_pos = copy.deepcopy(new_line_init_pos)

            # Mirror the end position horizontally
            line_end_pos = copy.deepcopy(zline_nju_ops.line_end_pos)
            new_line_end_pos = []
            for pos in line_end_pos:
                new_pos = (-pos[0], pos[1])  # Horizontal mirror operation (negate x-coordinate)
                new_line_end_pos.append(copy.deepcopy(new_pos))
            new_zline_nju_ops.line_end_pos = copy.deepcopy(new_line_end_pos)

            # Add the mirrored components to the collection
            zline_njus_ops[new_name] = copy.deepcopy(new_zline_nju_ops)

        # Inject the updated set of component parameters
        self.inject_options(zline_njus_ops)
        return
