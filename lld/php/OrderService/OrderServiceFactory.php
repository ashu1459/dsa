<?php

use Services\FSM;
use Services\FSMInterface;
use Services\Status\StatusInterface;
use Services\Events\EventsInterface;

Class OrderServiceFactory {
    /**
     * @return StatusInterface
     */
    public function createStatus(): StatusInterface {
        return new Status();
    }

    /**
     * @return EventsInterface
     */
    public function createEvents(): EventsInterface {
        return new Events();
    }

    /**
     * @return FSMInterface
     */
    public function createFSM($orderId): FSMInterface {
        # use the order-id to initialize FSM
        return new FSM(
            $orderId,
            $this->createStatus(),
            $this->createEvents()
        );
    }
}