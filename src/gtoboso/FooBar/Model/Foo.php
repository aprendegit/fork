<?php

namespace gtoboso\FooBar\Model;

class Foo extends Bar implements FooInterface
{
    /**
     * @var array
     */
    private $collection;

    public function __construct($lala)
    {
        parent::__construct($lala);

        $this->collection = array();
    }
    /**
     * @inheritdoc
     */
    public function foo1($param1, $param2, $forceSum = false)
    {
        $result = 0;

        if (true === $forceSum) {
            $result = $param1 + $param2;
        }

        return $result;
    }

    /**
     * @inheritdoc
     */
    public function foo2($param1, $param2)
    {
        return null;
    }

    protected function doAnything()
    {
        $sum = 1 + 1;
        $this->collection[] = $sum;
    }

}
