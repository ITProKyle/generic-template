Example Page
============

Plain text with some ``inline code``.

    quote block

.. code-block:: python
    :linenos:

    """Showcase custom pygments style."""
    # this is just an example
    import boto3

    client = boto3.client('ec2')
    print('client.describe_instances')
    print('test\ntest')

    def function(**kwarg):
        """placeholder."""

    class Test:
        """placeholder."""

        def __init__(self):
            """placeholder."""
            pass


+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

.. note:: This is a note.

.. important:: This is important.

.. warning:: This is a warning.

.. danger:: This is dangerous.


#. list item

* another list
