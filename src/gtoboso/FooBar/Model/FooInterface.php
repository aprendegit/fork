<?php

namespace gtoboso\FooBar\Model;

interface FooInterface
{
    /**
     * Do something witm params
     *
     * @param type $param1
     * @param type $param2
     * @param type $forceSum
     */
    public function foo1($param1, $param2, $forceSum = false);

    /**
     * Do something with params
     *
     * @param type $param1
     * @param type $param2
     *
     * @return null
     */
    public function foo2($param1, $param2);
}
