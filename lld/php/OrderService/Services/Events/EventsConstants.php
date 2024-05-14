<?php

namespace Services\Events;

Class EventsConstants {
    public const INIT = 'INIT';
    public const PAYMENT_RECEIVED = 'PAYMENT_RECEIVED';
    public const DISPATCH = 'DISPATCH';
    public const SHIP = 'SHIP';
    public const DELIVER = 'DELIVER';
    public const COMPLETE = 'COMPLETE';
    public const CANCEL = 'CANCEL';

    /**
     * @return array List of Statuses
     */
    public static function getAllEvents() {
        return [
            self::INIT,
            self::PAYMENT_RECEIVED,
            self::DISPATCH,
            self::SHIP,
            self::DELIVER,
            self::COMPLETE,
            self::CANCEL
        ];
    }

    /**
     * @param string $event
     * 
     * @return bool
     */
    public static function eventsExists($event) {
        return in_array($event, self::getAllEvents());
    }
}